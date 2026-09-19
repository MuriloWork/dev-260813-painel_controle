import os, re
import sys
import datetime
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'utils' / 'init_utils'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'utils' / 'io_utils'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'models'))
import parse_utils
import parse_export
import painel_settings as ps
from raw_script_model import RawScriptRow, RawScriptEntry

def parse_script(filepath, output_options, desired_comment_start=90):
    """Parses a script file to extract lines, comments, and tags, and
      performs actions based on output_options.
      """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        file_extension = os.path.splitext(filepath)[1].lower()
        comment_indicators = {
            '.py': '##',
            '.dart': '///'
        }
        
        # Determine the comment string for the current file type
        comment_str = comment_indicators.get(file_extension)
        if not comment_str:
            print(f"Warning: Unsupported file type '{file_extension}' for {filepath}. Skipping.")
            return []

        processed_data = []
        new_lines_for_alignment = [] # Used for alignment output option

        for line_num, line_content in enumerate(lines):
            original_line = line_content.rstrip('\n') # Remove trailing newline for processing
            
            script_string = original_line.lstrip()
            comment = ""
            tag = ""
            # Calculate column for the first non-whitespace character of the entire line
            first_char_index = len(original_line) - len(original_line.lstrip())
            # If the line is not empty or just whitespace, set column to 1-based index, otherwise 0
            column = first_char_index + 1 if original_line.lstrip() else 0 

            comment_start_index = original_line.find(comment_str)
            
            # Check if it's a secondary comment (not starting the line and comment_str found)
            if comment_start_index != -1 and not original_line.lstrip().startswith(comment_str):
                code_part = original_line[:comment_start_index].rstrip()
                comment_part_full = original_line[comment_start_index:].lstrip()
                
                # Extract the actual comment text, removing the indicator
                comment = comment_part_full[len(comment_str):].strip()
                script_string = code_part # The code part without the comment

                # Extract tag from comment
                tag_match = re.search(r'\[(.*?)\]', comment)
                if tag_match:
                    tag = tag_match.group(1).strip()
                    # Remove tag from comment text
                    comment = comment.replace(tag_match.group(0), '').strip()
                
                # A coluna já foi calculada, não é necessário recalcular aqui para o comentário secundário.
                # A coluna será a do primeiro caractere da linha.

                # Prepare line for alignment if that option is enabled
                if 'align_comments' in output_options:
                    padding_needed = max(0, desired_comment_start - len(code_part))
                    new_lines_for_alignment.append(code_part + ' ' * padding_needed + comment_part_full + '\n')
                else:
                    new_lines_for_alignment.append(original_line + '\n') # Keep original if no alignment
            else:
                new_lines_for_alignment.append(original_line + '\n') # Keep original for non-secondary comments

            processed_data.append({
                'line': line_num + 1, # 1-based line number
                'column': column,
                'script_string': script_string,
                'comment': comment,
                'tag': tag,
                'length': len(script_string)
            })
        
        # If alignment option is requested, rewrite the file
        if 'align_comments' in output_options:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines_for_alignment)
            # print(f"Comentários alinhados no arquivo '{filepath}'.")

        return processed_data

    except FileNotFoundError:
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao processar '{filepath}': {e}")
        return []

def process_scripts_main(
        input_paths, 
        output_options, 
        csv_output_path=None, 
        sqlite_db_path=None, 
        json_output_dir=None,
        table_name=None, 
        session_version=datetime.datetime.now().isoformat(), 
        desired_comment_start=90,
        source_config=None):
    """
    Main function to orchestrate the script parsing and output generation.
    Takes input paths (files/dirs) and output options.
    """

    found_file_infos = parse_utils.get_files_from_paths(
        input_paths,
        extensions=tuple(source_config.get('extensions', ['.py', '.dart'])) if source_config else ('.py', '.dart'),
        include_child_paths=source_config.get('include_child_paths') if source_config else None,
        include_child_globs=source_config.get('include_child_globs') if source_config else None,
        exclude_child_paths=source_config.get('exclude_child_paths') if source_config else None,
        exclude_child_globs=source_config.get('exclude_child_globs') if source_config else None,
    )
    if not found_file_infos:
        print("No Python or Dart files found to process.")
        return

    all_processed_data = []
    compact_version = session_version.replace(':', '').replace('-', '')

    for f_info in found_file_infos:
        filepath = f_info['filepath']
        original_input_path = f_info['original_input_path']
        is_directory_input = f_info['is_directory_input']

        # folder_path, file_path_for_output = get_output_paths(filepath, original_input_path, is_directory_input)
        folder_path, file_path_for_output = parse_utils.get_output_paths(filepath, original_input_path, is_directory_input)
        file_path_for_output = file_path_for_output.replace('\\', '/')

        options_for_parse_script = []
        if 'align_comments' in output_options:
            options_for_parse_script.append('align_comments')

        processed_data_for_file = parse_script(filepath, options_for_parse_script, desired_comment_start)

        project_root_name = Path(ps.PAINEL_ROOT).parent.name

        for item in processed_data_for_file:
            item['version'] = compact_version
            item['folder_path'] = folder_path
            item['file_path'] = file_path_for_output
            item['project_name'] = project_root_name
            all_processed_data.append(item)

        if 'json' in output_options:
            validated_rows = parse_export.validate_to_model(processed_data_for_file, RawScriptRow)
            sanitized_path = file_path_for_output.replace('\\', '^').replace('/', '^')
            base_ext = os.path.splitext(sanitized_path)
            if base_ext[1].lower() in ('.dart', '.py'):
                sanitized_path = base_ext[0] + '.json'
            json_filename = f"{compact_version}_{sanitized_path}"
            os.makedirs(json_output_dir, exist_ok=True)
            file_json_path = os.path.join(json_output_dir, json_filename)
            with open(file_json_path, 'w', encoding='utf-8') as f:
                json.dump([r.model_dump() for r in validated_rows], f, indent=2, ensure_ascii=False)

    version_tag = session_version.replace(':', '-').replace('.', '-')

    if 'csv' in output_options:
        base, ext = os.path.splitext(csv_output_path)
        final_csv_path = f"{base}_{version_tag}{ext}"
        parse_export.write_to_csv(all_processed_data, final_csv_path)

    if 'sqlite' in output_options:
        final_sqlite_path = sqlite_db_path
        # Agrupa os dados por arquivo e converte para o formato adequado para write_to_sqlite
        grouped_data = {}
        for item in all_processed_data:
            key = (item['project_name'], item['version'], item['folder_path'], item['file_path'])
            if key not in grouped_data:
                grouped_data[key] = []

            # Extrai apenas os campos necessários para json_data
            json_entry = {
                'line': item['line'],
                'column': item['column'],
                'script_string': item['script_string'],
                'comment': item['comment'],
                'tag': item['tag'],
                'length': item['length']
            }
            grouped_data[key].append(json_entry)

        # Prepara os dados no formato esperado por write_to_sqlite
        data_for_sqlite = []
        for (project_name, version, folder_path, file_path), json_list in grouped_data.items():
            validated_list = parse_export.validate_to_model(json_list, RawScriptRow)
            json_data_str = json.dumps([r.model_dump() for r in validated_list], ensure_ascii=False)
            entry = RawScriptEntry(
                project_name=project_name,
                version=version,
                folder_path=folder_path,
                file_path=file_path,
                json_data=validated_list
            )
            data_for_sqlite.append({
                'project_name': entry.project_name,
                'version': entry.version,
                'folder_path': entry.folder_path,
                'file_path': entry.file_path,
                'json_data': json_data_str
            })

        # Debug: imprimir informações sobre os dados que serão salvos
        # print(f"Preparando para salvar {len(data_for_sqlite)} registros no banco de dados")
        # if data_for_sqlite:
        #     print(f"Exemplo de dado: {data_for_sqlite[0]}")

        print(f"Enviando {len(data_for_sqlite)} registros para o banco de dados (esperado: número de arquivos processados)")
        parse_export.write_to_sqlite(data_for_sqlite, final_sqlite_path, table_name)

def get_action_config(action):
    cfg = ps.get_action_config('parse_script_raw.py', action)
    if cfg is None:
        return None, None, None

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

    source_config = input_configs[0] if input_configs else None

    return input_paths, child_action, source_config

def get_optional_settings(action):
    cfg = ps.get_action_config('parse_script_raw.py', action)
    if cfg is None:
        return {}
    return cfg.get('optional_settings', {})

def resolve_input_paths(paths, base_dir):
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

def process_action_raw(action):
    input_paths, child_action, source_config = get_action_config(action)
    optional_settings = get_optional_settings(action)

    print(f"\n--- Configuração carregada ---")
    print(f"ACTION: {action}")
    print(f"INPUT_PATHS: {input_paths}")
    print(f"CHILD_ACTION: {child_action}")
    print(f"OPTIONAL_SETTINGS: {optional_settings}")
    print(f"--------------------------------\n")

    input_paths = resolve_input_paths(input_paths, ps.PAINEL_ROOT)

    output_opts = [ca for ca in (child_action or []) if ca in ('align_comments', 'csv', 'sqlite', 'json')]

    desired_comment_start = int(optional_settings.get('DESIRED_COMMENT_START', 100))
    sqlite_db_path = ps.DB_PARSE_DART or None

    csv_dir = ps.TARGET_RAW or None
    csv_output_path = str(Path(csv_dir) / 'parsed_scripts.csv') if csv_dir else None

    json_output_dir = ps.TARGET_RAW or None

    process_scripts_main(
        input_paths=input_paths,
        output_options=output_opts,
        csv_output_path=csv_output_path,
        sqlite_db_path=sqlite_db_path,
        json_output_dir=json_output_dir,
        table_name=ps.TB_RAW or 'raw_script',
        session_version=datetime.datetime.now().isoformat(),
        desired_comment_start=desired_comment_start,
        source_config=source_config
    )

def main():
    parser = argparse.ArgumentParser(description='Parser raw de scripts Dart/Python')
    parser.add_argument('--action', type=str, required=True, help='Ação a executar (ex: raw)')
    args = parser.parse_args()

    ps.load_environment_main()

    action = args.action
    if action == 'raw':
        process_action_raw(action)
    else:
        print(f"[ERRO] Action desconhecida: {action}")

if __name__ == '__main__':
    main()
