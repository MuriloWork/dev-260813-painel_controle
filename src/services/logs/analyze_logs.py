#!/usr/bin/env python3
"""
Script para baixar e analisar logs do emulador Android.
Uso:
    python analyze_logs.py --pull      # Baixar logs do emulador
    python analyze_logs.py --list      # Listar logs baixados
    python analyze_logs.py --cat       # Mostrar conteúdo do último log
    python analyze_logs.py --csv       # Exportar último log para CSV
    python analyze_logs.py --csv <arquivo>  # Exportar arquivo específico para CSV
"""

import os
import sys
import subprocess
import glob
import re
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'utils' / 'init_utils'))
import painel_settings as ps

ps.load_environment_main()

EMULATOR_LOG_PATH = "app_flutter/app_logs/"
PACKAGE_NAME = "com.example.flutter_app_251130"


def get_logs_dir():
    return Path(ps.PJ_DIR_LOGS_DOCS_SESSION)


def ensure_logs_dir():
    logs_dir = get_logs_dir()
    logs_dir.mkdir(parents=True, exist_ok=True)


def pull_logs():
    logs_dir = get_logs_dir()
    print("Baixando logs do emulador...")
    print(f"Origem: {EMULATOR_LOG_PATH}")
    print(f"Destino: {logs_dir}")

    try:
        result = subprocess.run(
            ["adb", "shell", "run-as", PACKAGE_NAME, "ls", "-la", EMULATOR_LOG_PATH],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            print(f"Erro ao listar: {result.stderr}")
            return

        output = result.stdout.strip()
        print(f"Arquivos encontrados:\n{output}")

        if not output or "No such" in output:
            print("Nenhum arquivo de log encontrado.")
            print("Execute o app e tente novamente.")
            return

        log_files = []
        for line in output.split('\n'):
            if '.log' in line:
                parts = line.split()
                if len(parts) >= 8:
                    log_files.append(parts[-1])

        if not log_files:
            print("Nenhum arquivo .log encontrado.")
            return

        for log_file in log_files:
            source = f"{EMULATOR_LOG_PATH}{log_file}"
            dest = logs_dir / log_file

            result = subprocess.run(
                ["adb", "shell", "run-as", PACKAGE_NAME, "cat", source],
                capture_output=True,
                text=True,
                check=False,
            )

            if result.returncode == 0 and result.stdout:
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(result.stdout)
                print(f"Baixado: {log_file}")
            else:
                print(f"Erro ao baixar {log_file}: {result.stderr}")

        print("Logs baixados com sucesso!")

    except Exception as e:
        print(f"Erro ao baixar logs: {e}")


def list_logs():
    logs_dir = get_logs_dir()
    ensure_logs_dir()

    log_files = sorted(logs_dir.glob("*.log"))

    if not log_files:
        print("Nenhum log baixado.")
        print("Execute: python analyze_logs.py --pull")
        return

    print(f"Logs em {logs_dir}:")
    for log_file in log_files:
        size = log_file.stat().st_size
        print(f"  {log_file.name} ({size:,} bytes)")


def cat_logs(log_file=None):
    logs_dir = get_logs_dir()
    ensure_logs_dir()

    if log_file is None:
        log_files = sorted(logs_dir.glob("*.log"))
        if not log_files:
            print("Nenhum log encontrado.")
            return
        log_file = log_files[-1]
    else:
        log_file = logs_dir / log_file

    if not log_file.exists():
        print(f"Log não encontrado: {log_file}")
        return

    print(f"=== {log_file.name} ===")
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        print(f.read())


def parse_log_line(line):
    """
    Parses a log line and returns a dictionary with structured fields.
    
    Novocom caso formato ( especial):
    log_level:INFO,timestamp:2026-02-21 11:01:28.842,class_method_line:DataController.loadData:294,tag:loadData_initial_start,logType:DataFlow,script_action:iniciando_carregamento,var_tableName:descricao_padrao_nova
    
    Caso especial: class_method_line = separar em class, method, line
    
    Formato antigo (compatível):
    2026-02-20 15:01:36.046,messageType:INFO,tag:loadData_background_complete,...
    """
    line = line.strip()
    if not line:
        return None
    
    result = {}
    
    # Verificar se é o novo formato (começa com log_level:)
    if line.startswith('log_level:') or line.startswith('INFO,') or line.startswith('ERROR,'):
        # Novo formato: log_level:...,timestamp:...,class_method_line:...,tag:...
        # Ou formato intermediário: INFO,timestamp,...
        
        # Normalizar: se começa com INFO, ou ERROR, adicionar prefixo
        if line.startswith('INFO,') or line.startswith('ERROR,'):
            # Converter para formato padrão
            level = line.split(',')[0]
            rest = ','.join(line.split(',')[1:])
            line = f'log_level:{level},{rest}'
        
        fields = line.split(',')
        
        for field in fields:
            if ':' in field:
                key, value = field.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # CASO ESPECIAL: class_method_line -> class, method, line
                if key == 'class_method_line':
                    # Formato: Class.method:line
                    if ':' in value:
                        class_method, line_num = value.rsplit(':', 1)
                        if '.' in class_method:
                            class_name, method_name = class_method.rsplit('.', 1)
                            result['class'] = class_name
                            result['method'] = method_name
                        else:
                            result['class'] = class_method
                            result['method'] = ''
                        result['line'] = line_num
                    else:
                        result['class_method_line'] = value
                
                # CASO ESPECIAL: file -> remover package prefix e (line:col)
                elif key == 'file':
                    # Remover "package:flutter_app_251130/" do início
                    if value.startswith('package:flutter_app_251130/'):
                        value = value[len('package:flutter_app_251130/'):]
                    # Remover a partir de "("
                    if '(' in value:
                        value = value.split('(')[0]
                    result['file'] = value
                
                else:
                    result[key] = value
        
        return result
    
    # Formato antigo: timestamp,messageType:...,tag:...
    parts = line.split(',', 1)
    if len(parts) < 2:
        return None
    
    timestamp = parts[0].strip()
    message = parts[1].strip()
    
    result = {'timestamp': timestamp}
    
    fields = message.split(',')
    
    for field in fields:
        if ':' in field:
            key, value = field.split(':', 1)
            key = key.strip()
            value = value.strip()
            result[key] = value
    
    return result


def get_display_dir():
    return Path(ps.PJ_DIR_LOGS_DOCS_DISPLAY)


def ensure_display_dir():
    display_dir = get_display_dir()
    display_dir.mkdir(parents=True, exist_ok=True)


def find_latest_log_file(logs_dir):
    """
    Encontra o arquivo de log mais recente baseado na data no nome.
    Considera o padrão: prefixo_data.ext (ex: logs_session_2026-02-21.log)
    """
    log_files = sorted(logs_dir.glob("*.log"))
    if not log_files:
        return None
    
    # Parsear data do nome do arquivo (formato: prefixo_YYYY-MM-DD.log)
    def extract_date(f):
        try:
            name = f.stem  # sem extensão
            # Procura por data no formato YYYY-MM-DD
            match = re.search(r'(\d{4}-\d{2}-\d{2})', name)
            if match:
                return datetime.strptime(match.group(1), '%Y-%m-%d')
        except:
            pass
        return datetime.min
    
    # Ordenar por data (mais recente primeiro)
    sorted_logs = sorted(log_files, key=extract_date, reverse=True)
    return sorted_logs[0] if sorted_logs else None


def export_to_csv(log_file=None):
    logs_dir = get_logs_dir()
    ensure_logs_dir()
    ensure_display_dir()
    
    # Se não especificar arquivo, pega o mais recente
    if log_file is None:
        log_file = find_latest_log_file(logs_dir)
        if log_file is None:
            print("Nenhum log encontrado.")
            return
    else:
        log_file = logs_dir / log_file

    if not log_file.exists():
        print(f"Log não encontrado: {log_file}")
        return

    # Destino fixo: logs_display.csv em PJ_DIR_LOGS_DOCS_DISPLAY
    csv_file = get_display_dir() / "logs_display.csv"

    print(f"Convertendo {log_file.name} para CSV...")
    print(f"Destino: {csv_file}")

    parsed_logs = []

    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parsed = parse_log_line(line)
            if parsed:
                parsed_logs.append(parsed)

    if not parsed_logs:
        print("Nenhuma linha válida encontrada para converter.")
        return

    all_keys = set()
    for log in parsed_logs:
        all_keys.update(log.keys())

    priority_keys = ['log_level', 'timestamp', 'file', 'class', 'method', 'line', 'tag', 'logType', 'script_action']
    sorted_keys = priority_keys + sorted([k for k in all_keys if k not in priority_keys])

    with open(csv_file, "w", encoding="utf-8", newline='') as f:
        f.write(','.join(sorted_keys) + '\n')

        for log in parsed_logs:
            row = [str(log.get(k, '')) for k in sorted_keys]
            row = [f'"{r.replace("\"", "\"\"")}"' if ',' in r or '"' in r else r for r in row]
            f.write(','.join(row) + '\n')

    print(f"CSV salvo em: {csv_file}")
    print(f"Total de registros: {len(parsed_logs)}")


def main():
    """
    Script para baixar e analisar logs do emulador Android.
    Uso:
        python analyze_logs.py --pull      # Baixar logs do emulador
        python analyze_logs.py --list      # Listar logs baixados
        python analyze_logs.py --cat       # Mostrar conteúdo do último log
        python analyze_logs.py --csv       # Exportar último log para CSV
        python analyze_logs.py --csv <arquivo>  # Exportar arquivo específico para CSV
        python analyze_logs.py --all       # Executar pull + csv (baixar e exportar)
        python analyze_logs.py "--pull --csv"  # Múltiplas ações
    """
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    # Separa as ações (pode vir como string única "pull csv" ou lista ["--pull", "--csv"])
    raw_args = sys.argv[1:]
    commands = []
    for arg in raw_args:
        # Se o argumento contém espaços ou vírgulas, divide em múltiplas ações
        if ' ' in arg or ',' in arg:
            # Substitui vírgulas por espaços e divide
            parts = arg.replace(',', ' ').split()
            commands.extend(parts)
        else:
            commands.append(arg)
    
    # Normaliza: adiciona "--" antes de cada ação se não tiver
    normalized_commands = []
    for cmd in commands:
        if not cmd.startswith('--'):
            cmd = '--' + cmd
        normalized_commands.append(cmd)
    commands = normalized_commands
    
    # Executar todos os comandos passados
    for command in commands:
        command = command.lower()
        
        if command == "--pull":
            pull_logs()
        elif command == "--list":
            list_logs()
        elif command == "--cat":
            log_file = None
            # Procura --csv seguido de nome de arquivo na lista de argumentos
            idx = commands.index(command)
            if idx + 1 < len(commands) and not commands[idx + 1].startswith('--'):
                log_file = commands[idx + 1]
            cat_logs(log_file)
        elif command == "--csv":
            log_file = None
            # Procura --csv seguido de nome de arquivo na lista de argumentos
            idx = commands.index(command)
            if idx + 1 < len(commands) and not commands[idx + 1].startswith('--'):
                log_file = commands[idx + 1]
            export_to_csv(log_file)
        elif command == "--all":
            # pull + csv
            pull_logs()
            export_to_csv()
        else:
            print(f"Comando desconhecido: {command}")
            print(__doc__)
            sys.exit(1)


if __name__ == "__main__":
    main()
