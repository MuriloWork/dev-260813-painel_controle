import os
import subprocess
from pathlib import Path
from datetime import datetime
import json
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'utils' / 'init_utils'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'models'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'utils' / 'io_utils'))
import parse_utils
import parse_export
import painel_sqlite_import
import painel_sqlite_export
import painel_settings as ps
from ast_dart_model import AstNode


def _upsert_shell_target(target_key, target_data, shell_targets_path):
    return  # Temporariamente desabilitado
    """ Faz upsert de configuração em set_shell_targets.json """
    targets = []
    
    if os.path.exists(shell_targets_path):
        with open(shell_targets_path, 'r', encoding='utf-8') as f:
            targets = json.load(f)
    
    # Busca índice do item com mesmo description
    existing_index = -1
    for i, t in enumerate(targets):
        if t.get('description') == target_data.get('description'):
            existing_index = i
            break
    
    now = datetime.now().isoformat()
    target_data['metadata'] = target_data.get('metadata', {})
    target_data['metadata']['updateTimestamp'] = now
    
    if existing_index >= 0:
        # Update: mantém firstInsertTimestamp original
        target_data['metadata']['firstInsertTimestamp'] = targets[existing_index].get('metadata', {}).get('firstInsertTimestamp', now)
        targets[existing_index] = target_data
    else:
        # Insert
        target_data['metadata']['firstInsertTimestamp'] = now
        targets.append(target_data)
    
    with open(shell_targets_path, 'w', encoding='utf-8') as f:
        json.dump(targets, f, indent=4, ensure_ascii=False)
    
    print(f"[OK] Shell target atualizado: {target_data.get('description', target_key)}")


def _register_shell_target(shell_targets_path):
    return  # Temporariamente desabilitado
    """Registra parse_dart_ast.py em shell_targets.json"""
    target_key = "parse_dart_ast"

    target_data = {
        "description": "Executar parse_dart_ast.py - Parser AST de arquivos Dart",
        "type": "python",
        "scriptPath": "dev/painel/parse/parse_dart_ast.py",
        "arguments": "--dart_dir $ps.PJ_DART_DIR --output $OUTPUT_OPTIONS",
        "placeholders": [
            {"name": "ps.PJ_DART_DIR", "prompt": "Diretório dos arquivos Dart:", "default": ps.SOURCE_DART},
            {"name": "OUTPUT_OPTIONS", "prompt": "Opções de saída (csv,sqlite):", "default": "sqlite"}
        ],
        "metadata": {}
    }

    _upsert_shell_target(target_key, target_data, shell_targets_path)


def get_env(key, default=''):
    """Helper para obter variável de ambiente com default."""
    return os.environ.get(key, default)


def _ensure_dart_dependencies():
    """Verifica e instala dependências Dart se necessário."""
    pubspec_path = Path(ps.PAINEL_DART_TOOLS_DIR) / 'pubspec.yaml'
    publock_path = Path(ps.PAINEL_DART_TOOLS_DIR) / 'pubspec.lock'
    
    if not publock_path.exists():
        print(f"[INFO] Instalando dependências Dart em: {ps.PAINEL_DART_TOOLS_DIR}")
        try:
            result = subprocess.run(
                [ps.ABS_PATH_DART_EXECUTABLE, 'pub', 'get'],
                cwd=ps.PAINEL_DART_TOOLS_DIR,
                capture_output=True,
                text=True,
                timeout=120
            )
            if result.returncode == 0:
                print("[OK] Dependências Dart instaladas")
            else:
                print(f"[ERRO] Falha ao instalar dependências: {result.stderr}")
        except Exception as e:
            print(f"[ERRO] Exception ao instalar dependências: {e}")


def get_action_config(action):
    cfg = ps.get_action_config('parse_script_dart_ast.py', action)
    if cfg is None:
        return None, None, None, None
    
    child_action = cfg.get('child_action', [])

    input_refs = [i.get('var_ref', '') for i in cfg.get('input', [])]
    input_configs = []
    input_paths = []
    for ref in input_refs:
        config = getattr(ps, f'{ref}_CONFIG', None)
        if config:
            input_paths.extend(config.get('paths', []))
            input_configs.append(config)
        else:
            val = getattr(ps, ref, '')
            if val:
                input_paths.append(val)
            input_configs.append(None)

    output_options = [o.get('output_name', '') for o in cfg.get('output', [])]

    source_config = input_configs[0] if input_configs else None

    return input_paths, output_options, child_action, source_config


def get_optional_settings(action):
    cfg = ps.get_action_config('parse_script_dart_ast.py', action)
    if cfg is None:
        return {}
    return cfg.get('optional_settings', {})


def generate_ast_for_file(dart_file_path, project_root, dart_executable_path, dart_sdk_path):
    """
    Executa o processo para gerar o AST de um único arquivo Dart.
    """
    dart_file_str = str(dart_file_path)
    project_root_str = str(project_root)

    print(f"Generating resolved AST for {dart_file_str}...")
    print(f"[DEBUG] dart_executable_path: '{dart_executable_path}'")
    print(f"[DEBUG] project_root_str: '{project_root_str}'")
    print(f"[DEBUG] dart_sdk_path: '{dart_sdk_path}'")
    print(f"[DEBUG] PAINEL_DART_TOOLS_DIR: '{ps.PAINEL_DART_TOOLS_DIR}'")
    print(f"[DEBUG] cwd exists: {os.path.exists(ps.PAINEL_DART_TOOLS_DIR)}")
    print(f"[DEBUG] dart.exe exists: {os.path.exists(dart_executable_path)}")
    try:
        command = [
            dart_executable_path, "run", "parse_dart_ast.dart",
            dart_file_str, project_root_str, dart_sdk_path
        ]
        print(f"[DEBUG] command list: {command}")

        result = subprocess.run(
            command,
            cwd=ps.PAINEL_DART_TOOLS_DIR,
            capture_output=True,
            text=True,
            check=True,
            encoding="utf-8"
        )
        data = json.loads(result.stdout)
        AstNode.model_validate(data)
        return data
    except subprocess.CalledProcessError as e:
        print(f"Error generating resolved AST for {dart_file_str}: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for {dart_file_str}: {e}")
        print(f"Raw output from subprocess: {result.stdout}")
        return None
    except FileNotFoundError:
        print(f"Error: O diretório de trabalho '{ps.PAINEL_DART_TOOLS_DIR}' para o subprocesso não foi encontrado.")
        return None


def resolve_input_paths(paths, base_dir):
    """
    Converte caminhos relativos para absolutos usando base_dir como referência.
    """
    if not paths or not base_dir:
        return paths
    
    resolved = []
    for p in paths:
        if p and not os.path.isabs(p):
            p_normalized = p.replace('/', os.sep).replace('\\', os.sep)
            resolved_path = os.path.join(base_dir, p_normalized)
            resolved.append(resolved_path)
        else:
            resolved.append(p)
    return resolved


def process_ast_files(all_dart_files, session_version):
    """
    Processa os arquivos Dart gerando AST e salvando em JSON.
    """
    project_root = ps.PAINEL_ROOT
    dart_executable_path = ps.ABS_PATH_DART_EXECUTABLE
    dart_sdk_path = ps.ABS_PATH_DART_SDK
    
    print(f"Processando {len(all_dart_files)} arquivos para análise AST...")
    for dart_file_path in all_dart_files:
        if not str(dart_file_path).lower().endswith('.dart'):
            continue
        dart_file = Path(dart_file_path)
        
        json_data = generate_ast_for_file(dart_file, project_root, dart_executable_path, dart_sdk_path)
        
        if json_data:
            timestamp_str = session_version.replace(':', '').replace('-', '')
            dart_dir_str = str(ps.SOURCE_DART).rstrip('\\/')
            dart_file_str = str(dart_file).rstrip('\\/')
            if dart_file_str.startswith(dart_dir_str):
                relative_path = dart_file_str[len(dart_dir_str):].lstrip('\\/')
            else:
                relative_path = Path(dart_file).name
            relative_path_str = relative_path.replace('\\', '^').replace('/', '^').replace('.dart', '.json')
            json_filename = f"{timestamp_str}_{relative_path_str}"
            
            json_output_path = Path(ps.TARGET_DART) / json_filename
            os.makedirs(json_output_path.parent, exist_ok=True)
            parse_export.write_to_json(json_data, str(json_output_path))


def process_action_ast_sqlite(action):
    """
    Processa action do tipo ast_sqlite (ast_sqlite, ast_sqlite_ast, etc).
    Faz upsert, executa triggers e exporta dados do SQLite.
    """
    input_paths, output_options, child_action, _ = get_action_config(action)
    optional_settings = get_optional_settings(action)
    
    print(f"\n--- Configuração carregada ---")
    print(f"ACTION: {action}")
    print(f"CHILD_ACTION: {child_action}")
    print(f"OPTIONAL_SETTINGS: {optional_settings}")
    print(f"--------------------------------\n")
    
    for child in (child_action or []):
        if child == 'sqlite_upsert':
            painel_sqlite_import.upsert_sqlite(
                sqlite_db_path=ps.DB_PARSE_DART,
                table_name=ps.TB_AST
            )
            print(f"Upsert concluído no banco de dados.")
        
        elif child == 'sqlite_triggers':
            # Pegar settings específico para sqlite_triggers
            trigger_settings = optional_settings.get('sqlite_triggers')
            painel_sqlite_import.sqlite_triggers(
                sqlite_db_path=ps.DB_PARSE_DART,
                action=action,
                steps_to_execute=trigger_settings
            )
            print(f"Triggers executados com sucesso.")
        
        elif child == 'sqlite_export_ast':
            # Pegar settings específico para sqlite_export_ast
            try:
                export_settings = optional_settings.get('sqlite_export_ast', [])
                print(f"[DEBUG] sqlite_export_ast - export_settings: {export_settings}")
                if export_settings:
                    print(f"[DEBUG] Chamando painel_sqlite_export.main com: {export_settings}")
                    painel_sqlite_export.main(export_settings)
                    print(f"Exportação de dados concluída.")
                else:
                    print(f"[DEBUG] export_settings vazio, pulando exportação")
            except Exception as e:
                print(f"[ERRO] Falha ao executar sqlite_export_ast: {e}")
                import traceback
                traceback.print_exc()
    
    print("Processo de análise AST concluído.")


def process_action_ast(action):
    """
    Processa action do tipo ast (ast, ast_json).
    Lê child_action e optional_settings dinamicamente do JSON.
    """
    input_paths, output_options, child_action, source_config = get_action_config(action)
    optional_settings = get_optional_settings(action)
    
    print(f"\n--- Configuração carregada ---")
    print(f"ACTION: {action}")
    print(f"INPUT_PATHS: {input_paths}")
    print(f"OUTPUT_OPTIONS: {output_options}")
    print(f"CHILD_ACTION: {child_action}")
    print(f"OPTIONAL_SETTINGS: {optional_settings}")
    print(f"--------------------------------\n")
    
    for child in (child_action or []):
        print(f"[DEBUG] Processando child_action: {child}")
        if child == 'json':
            if not input_paths:
                input_paths = [ps.SOURCE_DART]
            input_paths = resolve_input_paths(input_paths, ps.SOURCE_DART)
            
            print("Encontrando arquivos Dart para análise AST...")
            dart_file_infos = parse_utils.get_files_from_paths(
                input_paths,
                extensions=tuple(source_config.get('extensions', ['.py', '.dart'])) if source_config else ('.py', '.dart'),
                include_child_paths=source_config.get('include_child_paths') if source_config else None,
                include_child_globs=source_config.get('include_child_globs') if source_config else None,
                exclude_child_paths=source_config.get('exclude_child_paths') if source_config else None,
                exclude_child_globs=source_config.get('exclude_child_globs') if source_config else None,
            )
            all_dart_files = [info['filepath'] for info in dart_file_infos]
            
            session_version = datetime.now().isoformat()
            
            process_ast_files(
                all_dart_files=all_dart_files,
                session_version=session_version
            )
        
        elif child == 'sqlite_upsert':
            painel_sqlite_import.upsert_sqlite(
                sqlite_db_path=ps.DB_PARSE_DART,
                table_name=ps.TB_AST
            )
            print(f"Upsert concluído no banco de dados.")
        
        elif child == 'sqlite_triggers':
            # Pegar settings específico para sqlite_triggers
            trigger_settings = optional_settings.get('sqlite_triggers')
            painel_sqlite_import.sqlite_triggers(
                sqlite_db_path=ps.DB_PARSE_DART,
                action=action,
                steps_to_execute=trigger_settings
            )
            print(f"Triggers executados com sucesso.")
        
        elif child == 'sqlite_export_ast':
            # Pegar settings específico para sqlite_export_ast
            try:
                export_settings = optional_settings.get('sqlite_export_ast', [])
                print(f"[DEBUG] sqlite_export_ast - export_settings: {export_settings}")
                if export_settings:
                    print(f"[DEBUG] Chamando painel_sqlite_export.main com: {export_settings}")
                    painel_sqlite_export.main(export_settings)
                    print(f"Exportação de dados concluída.")
                else:
                    print(f"[DEBUG] export_settings vazio, pulando exportação")
            except Exception as e:
                print(f"[ERRO] Falha ao executar sqlite_export_ast: {e}")
                import traceback
                traceback.print_exc()
    
    print("Processo de análise AST concluído.")


def main():
    """Orquestra o processo de análise de AST."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Parser AST de arquivos Dart')
    parser.add_argument('--action', type=str, required=True, help='Ação a executar (ex: ast, raw)')
    
    args = parser.parse_args()
    
    ps.load_environment_main()
    
    print(f"[DEBUG] After load - ps.PAINEL_ROOT: {ps.PAINEL_ROOT}")
    print(f"[DEBUG] After load - ps.SOURCE_DART: {ps.SOURCE_DART}")
    
    _ensure_dart_dependencies()
    
    action = args.action
    if action in ['ast', 'ast_json']:
        process_action_ast(action)
    elif action.startswith('sqlite') or action in ['ast_sqlite']:
        process_action_ast_sqlite(action)
    else:
        print(f"[ERRO] Action desconhecida: {action}")


if __name__ == "__main__":
    main()
