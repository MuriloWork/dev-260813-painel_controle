#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para aplicacao automatica de logs em codigo Dart.
Le configuracoes de logs e aplica tags no codigo Dart por substituicao direta.
"""

import json
import re
import os
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class LogString:
    """Representa uma definicao de log string."""
    log_name: str
    placeholders_txt: Dict[str, Dict[str, str]] = field(default_factory=dict)
    placeholders_var: Dict[str, Dict[str, str]] = field(default_factory=dict)


@dataclass
class TagMapping:
    """Representa um mapeamento de tag para log."""
    tag_name: str
    log_name: str
    class_name: str = ""
    method: str = ""
    placeholders_txt: Dict[str, str] = field(default_factory=dict)
    placeholders_var_remove: Optional[List[str]] = field(default_factory=list)


class LogInserter:
    """Classe responsavel por inserir logs em codigo Dart."""
    
    def __init__(self, config_dir: str):
        self.config_dir = Path(config_dir)
        self.log_strings: Dict[str, LogString] = {}
        self.tag_mappings: Dict[str, TagMapping] = {}
        self.load_configs()
    
    def load_configs(self):
        """Carrega as configuracoes de logs."""
        # Carregar logs_string.json
        logs_file = self.config_dir / "logs_string.json"
        with open(logs_file, 'r', encoding='utf-8') as f:
            logs_data = json.load(f)
            for log_def in logs_data:
                self.log_strings[log_def['log_name']] = LogString(
                    log_name=log_def['log_name'],
                    placeholders_txt=log_def.get('placeholders_txt', {}),
                    placeholders_var=log_def.get('placeholders_var', {})
                )
        
        # Carregar logs_current_tag_map.json
        tags_file = self.config_dir / "logs_current_tag_map.json"
        with open(tags_file, 'r', encoding='utf-8') as f:
            tags_data = json.load(f)
            for tag_def in tags_data:
                # Usa tag_name como chave para permitir múltiplos mappings para o mesmo log_name
                self.tag_mappings[tag_def['tag_name']] = TagMapping(
                    tag_name=tag_def['tag_name'],
                    log_name=tag_def['log_name'],
                    class_name=tag_def.get('class', ''),
                    method=tag_def.get('method', ''),
                    placeholders_txt=tag_def.get('placeholders_txt', {}),
                    placeholders_var_remove=tag_def.get('placeholders_var_remove') or []
                )
    
    def get_log_for_tag(self, tag_string: str) -> Optional[Tuple[LogString, TagMapping]]:
        """Retorna a definicao de log e mapeamento para uma tag_string."""
        mapping = self.tag_mappings.get(tag_string)
        if mapping:
            log_def = self.log_strings.get(mapping.log_name)
            if log_def:
                return (log_def, mapping)
        return None

    def build_log_string(self, log_name: str, tag_name: Optional[str] = None, match: Optional[object] = None, content: Optional[str] = None) -> str:
        """
        Constrói a string de log dinamicamente usando os modelos JSON.
        
        Processo:
        1. Pegar config do logs_string (placeholders_txt + placeholders_var)
        2. Pegar valores do tag_map (placeholders_txt + placeholders_var_remove)
        3. Construir parte fixa (placeholders_txt) com valores do tag_map
        4. Adicionar parte variável (placeholders_var), aplicando remoções
        
        Args:
            log_name: Nome do log
            tag_name: Nome da tag específica
            match: Objeto match do regex
            content: Conteúdo do arquivo Dart (para determinar se é comentário ou logger)
        """
        # Verificar se é comentário ou logger
        is_logger = False
        if match and content:
            pos = match.start()
            # Se antes tem "Logger.info(" é logger, senão é comentário
            if pos >= 13 and content[pos-13:pos] == "Logger.info(":
                is_logger = True
        
        log_def = self.log_strings.get(log_name)
        if not log_def:
            return ""
        
        # Se tag_name especificado, usar para buscar o mapping correto
        tag_map = None
        if tag_name:
            tag_map = self.tag_mappings.get(tag_name)
        else:
            # Buscar primeiro mapping com esse log_name
            for tn, mapping in self.tag_mappings.items():
                if mapping.log_name == log_name:
                    tag_map = mapping
                    break
        
        if not tag_map:
            return ""
        
        # 1. Construir parte fixa (placeholders_txt) - vem do tag_map
        partes_txt = []
        for key, config in log_def.placeholders_txt.items():
            if config.get("source") == "tag_map":
                key_no_prefix = config.get("key", key)
                # Casos especiais: tag_name vem do campo root do TagMapping
                if key_no_prefix == "tag_name":
                    valor = tag_map.tag_name
                else:
                    valor = tag_map.placeholders_txt.get(key_no_prefix, "")
                partes_txt.append(f"{key}:{valor}")
        
        # 2. Construir parte variável (placeholders_var) - runtime
        partes_var = []
        for key, config in log_def.placeholders_var.items():
            # Verificar se não foi removido pelo tag_map
            if tag_map.placeholders_var_remove and key in tag_map.placeholders_var_remove:
                continue
            
            # Usar key e value explícitos do config
            var_key = config.get("key", key)
            var_value = config.get("value", f"{{{key}}}")
            partes_var.append(f"var_{var_key}:{var_value}")
        
        # 3. Montar string final
        todas_partes = partes_txt + partes_var
        result = ",".join(todas_partes)
        
        # Se é logger (não é comentário), adicionar vírgula no final
        if is_logger:
            result = result + ","
        
        return result
    
    def extract_variables_from_code(self, content: str, position: int, tag_name: str) -> Dict[str, str]:
        """Extrai variaveis do contexto do codigo Dart."""
        vars_dict = {}
        
        # Tag name para identificacao
        vars_dict['tag_name'] = tag_name
        
        # Pegar conteudo ate a posicao da tag
        code_before = content[:position]
        
        # Extrair line - procurar pelo numero da linha no contexto
        # Procura por "line:XXX" no codigo antes da tag
        line_match = re.search(r'line[:\s]+(\d+)', code_before, re.IGNORECASE)
        if line_match:
            vars_dict['line'] = line_match.group(1)
        
        # Extrair acao - deve ser definida via mapping.placeholder_values
        # Nao faz parte de extract_variables_from_code, vem do mapping
        
        # Extrair tableName
        vars_dict['tableName'] = "${dataContext.selectedTableName}"
        
        # Extrair limit e offset (valores tipicos)
        vars_dict['limit'] = "${dataContext.itemsPerPage}"
        vars_dict['offset'] = "${0}"
        
        # Contagem de registros
        vars_dict['count'] = "${result.data.length}"
        vars_dict['total'] = "${dataStore.currentTableDataFinal.length}"
        
        # hasMore
        vars_dict['hasMore'] = "${result.hasMoreData}"
        
        # Erro
        vars_dict['error'] = "${e.toString()}"
        
        # Preserve scroll
        vars_dict['preserve'] = "${showWithScroll}"
        
        return vars_dict
    
    def resolve_placeholders(self, log_string: str, text_values: Dict[str, str], 
                           var_values: Dict[str, str]) -> str:
        """Resolve os placeholders em uma log string."""
        result = log_string
        
        # Primeiro resolve valores de texto (da tag)
        for key, value in text_values.items():
            placeholder = "{" + key + "}"
            result = result.replace(placeholder, value)
        
        # Depois resolve variaveis (do codigo) - substitui placeholder pela expressao Dart
        for key, value in var_values.items():
            placeholder = "{" + key + "}"
            # Se ainda nao foi substituido (era uma var, nao um texto)
            if placeholder in result:
                result = result.replace(placeholder, value)
        
        return result
    
    def extract_log_key(self, log_string: str) -> str:
        """
        Extrai a 'chave' de um log_string para busca no codigo Dart.
        Usa apenas o campo 'tag' como chave de busca.
        """
        # Extrair tag do log_string
        match = re.search(r'tag:(\{tag_name\}|\w+)', log_string)
        if match:
            tag_value = match.group(1)
            # Se for placeholder, retornar o placeholder
            if tag_value == '{tag_name}':
                return 'tag:{tag_name}'
            # Se for valor fixo, retornar o valor
            return f'tag:{tag_value}'
        return ''
    
    def find_log_by_key(self, content: str, key: str, log_name: str) -> List[re.Match]:
        """
        Procura um log no codigo Dart pela tag_name.
        Retorna todos os matches encontrados para o log_name específico.
        """
        # Encontrar todas as tag_names correspondentes a este log_name
        tag_names = []
        for tag_string, mapping in self.tag_mappings.items():
            if mapping.log_name == log_name:
                tag_names.append(mapping.tag_name)
        
        if not tag_names:
            return []
        
        # Buscar por cada tag_name deste log_name
        matches = []
        for tag_name in tag_names:
            pattern = f'tag:{re.escape(tag_name)}'
            found = re.finditer(pattern, content)
            matches.extend(found)
        
        return matches
    
    def convert_logger_to_tags(self, dart_file: str) -> Tuple[int, int]:
        """
        Converte Logger.info em tags // tag_name:xxx.
        
        Returns:
            Tuple (loggers_encontrados, tags_criados)
        """
        with open(dart_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        loggers_found = 0
        tags_created = 0
        modifications = []
        
        # Procurar por Logger.info( até );
        pattern = r"Logger\.info\("
        matches = list(re.finditer(pattern, content))
        
        for match in matches:
            logger_start = match.start()
            
            # Encontrar o ); mais próximo após Logger.info(
            remaining = content[logger_start + len("Logger.info("):]
            semicolon_match = re.search(r"\);", remaining)
            if not semicolon_match:
                continue
            
            # logger_end deve incluir o );
            logger_end = logger_start + len("Logger.info(") + semicolon_match.start() + 2
            full_match = content[logger_start:logger_end]
            
            # Extrair tag_name da string de log
            tag_match = re.search(r'tag_name:([^,\s]+)', full_match)
            if not tag_match:
                continue
            
            loggers_found += 1
            tag_name = tag_match.group(1)
            
            # Verificar se mapping existe (tentar com e sem vírgula)
            if tag_name not in self.tag_mappings:
                if tag_name + ',' not in self.tag_mappings:
                    print(f"  AVISO: Tag '{tag_name}' não encontrado no mapping")
                    continue
                tag_name = tag_name + ','
            
            # Criar tag - adicionar newline para separar do código seguinte
            replacement = f"// tag_name:{tag_name}\n"
            
            modifications.append({
                'start': logger_start,
                'end': logger_end,
                'replacement': replacement,
                'source': f'logger_to_tag:{tag_name}'
            })
            tags_created += 1
            print(f"  OK: Logger.info('{tag_name}...') -> {replacement}")
        
        # Aplicar modificações em ordem reversa
        if modifications:
            modifications.sort(key=lambda x: x['start'], reverse=True)
            for mod in modifications:
                content = content[:mod['start']] + mod['replacement'] + content[mod['end']:]
            
            with open(dart_file, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return (loggers_found, tags_created)
    
    def log_upsert_on_selected_tag(self, dart_file: str) -> Tuple[int, int]:
        """
        Aplica logs no arquivo Dart.
        1. Primeiro tenta encontrar por tag // TAG: xxx
        2. Se não encontrar, busca pela chave extraída de log_string
        
        Returns:
            Tupla (logs_encontrados, logs_aplicados)
        """
        with open(dart_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        logs_found = 0
        logs_applied = 0
        modifications = []
        processed_positions = set()
        
        # Ordenar mappings por tag_name mais longo primeiro (para evitar match parcial)
        sorted_mappings = sorted(self.tag_mappings.items(), key=lambda x: len(x[1].tag_name), reverse=True)
        
        # Procurar por tag_name:tag_name
        for tag_name_key, mapping in sorted_mappings:
            # Primeiro: procurar por // tag_name:xxx (comentário - termina com ; ou newline)
            pattern_comment = f"tag_name:{re.escape(mapping.tag_name)}(;|\\n|$)"
            matches_comment = list(re.finditer(pattern_comment, content))
            
            for match in matches_comment:
                pos = match.start()
                if pos in processed_positions:
                    continue
                
                logs_found += 1
                processed_positions.add(pos)
                
                # build_log_string determina se é comentário ou logger
                log_str = self.build_log_string(mapping.log_name, mapping.tag_name, match, content)
                if not log_str:
                    continue
                
                final_log = f"Logger.info('{log_str}')"
                replacement = f"{final_log};\n"
                
                modifications.append({
                    'start': pos - 3,  # incluir //
                    'end': match.end(),
                    'replacement': replacement,
                    'source': f'tag:{mapping.tag_name}'
                })
                logs_applied += 1
                print(f"  OK: Tag '{mapping.tag_name}' -> log aplicado")
            
            # Segundo: procurar por tag_name:xxx, (logger.info - com vírgula)
            pattern_logger = f"tag_name:{re.escape(mapping.tag_name)},"
            matches_logger = list(re.finditer(pattern_logger, content))
            
            for match in matches_logger:
                pos = match.start()
                if pos in processed_positions:
                    continue
                
                logs_found += 1
                processed_positions.add(pos)
                
                # build_log_string determina se é comentário ou logger
                log_str = self.build_log_string(mapping.log_name, mapping.tag_name, match, content)
                if not log_str:
                    continue
                
                final_log = f"Logger.info('{log_str}')"
                
                # Substituir todo o Logger.info
                logger_start = content.rfind('Logger.info(', 0, pos)
                remaining = content[match.end():]
                semicolon_match = re.search(r';', remaining)
                end_pos = match.end() + semicolon_match.end() if semicolon_match else match.end()
                
                replacement = f"{final_log};\n"
                
                modifications.append({
                    'start': logger_start,
                    'end': end_pos,
                    'replacement': replacement,
                    'source': f'logger:{mapping.tag_name}'
                })
                logs_applied += 1
                print(f"  OK: Logger '{mapping.tag_name}' -> log aplicado")
        
        # Aplicar modificacoes em ordem reversa
        if modifications:
            modifications.sort(key=lambda x: x['start'], reverse=True)
            for mod in modifications:
                content = content[:mod['start']] + mod['replacement'] + content[mod['end']:]
            
            with open(dart_file, 'w', encoding='utf-8') as f:
                f.write(content)
        
        return (logs_found, logs_applied)


def main():
    """Função principal."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Aplicador de logs Dart')
    parser.add_argument('action', choices=['apply', 'revert'], default='apply',
                        help='acao: apply (tag -> logger) ou revert (logger -> tag)')
    args = parser.parse_args()
    
    # Configurar caminhos
    current_file = Path(__file__).resolve()
    logs_dir = current_file.parent
    config_dir = logs_dir.parent.parent / "config"
    dart_file = logs_dir.parent.parent.parent / "lib" / "controller" / "controller_second_screen.dart"
    
    print("=" * 60)
    print("APLICADOR DE LOGS DART v1.0")
    print("=" * 60)
    print(f"\nAcao: {args.action}")
    print(f"Configuracao: {config_dir}")
    print(f"Arquivo alvo: {dart_file}")
    print()
    
    # Verificar se arquivo existe
    if not dart_file.exists():
        print(f"ERRO: Arquivo nao encontrado: {dart_file}")
        return
    
    # Criar backup
    backup_file = dart_file.with_suffix('.dart.backup')
    with open(dart_file, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"OK: Backup criado: {backup_file}")
    print()
    
    inserter = LogInserter(str(config_dir))
    
    if args.action == 'revert':
        # Converter logger.info em tags
        loggers_found, tags_created = inserter.convert_logger_to_tags(str(dart_file))
        print(f"\nResumo:")
        print(f"  Loggers encontrados: {loggers_found}")
        print(f"  Tags criados: {tags_created}")
        if tags_created > 0:
            print("\n" + "=" * 60)
            print("OK: LOGS REVERTIDOS COM SUCESSO")
            print("=" * 60)
    else:
        # Aplicar logs (tag -> logger)
        tags_found, tags_applied = inserter.log_upsert_on_selected_tag(str(dart_file))
        print(f"\nResumo:")
        print(f"  Tags encontradas: {tags_found}")
        print(f"  Tags aplicadas: {tags_applied}")
        
        if tags_applied > 0:
            print("\n" + "=" * 60)
            print("OK: LOGS APLICADOS COM SUCESSO")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("AVISO: NENHUMA TAG ENCONTRADA OU APLICADA")
            print("=" * 60)
            print("\nCertifique-se de adicionar as tags manualmente no codigo:")
            for tag_string in inserter.tag_mappings.keys():
                print(f"  {tag_string}")


if __name__ == "__main__":
    main()
