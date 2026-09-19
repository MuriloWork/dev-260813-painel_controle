import os, sys, datetime, time, sqlite3, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'init_utils'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'models'))
import painel_settings as ps
from import_model import TagMapEntry, LogsStringEntry
from ast_dart_model import FlutterAppAst


def check_sqlite_available(db_path):
    """
    Função para verificar se o banco de dados SQLite está disponível
    Retorna True quando o banco estiver disponível
    """
    while True:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            conn.close()
            return True
        except sqlite3.Error:
            time.sleep(1)


def execute_sql_file(cursor, sql_file_path):
    """
    Função para executar um arquivo SQL no cursor fornecido
    """
    with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
        sql_commands = sql_file.read()
        cursor.executescript(sql_commands)


def sqlite_triggers(sqlite_db_path, action=None, steps_to_execute=None):
    if steps_to_execute is None:
        ps.load_environment_main()
        cfg = ps.get_action_config('parse_script_dart_ast.py', action or 'ast')
        if cfg:
            steps_to_execute = cfg.get('optional_settings', {}).get('sqlite_triggers_steps',
                ['tb_ast', 'tb_ast_func', 'tb_ast_func_map_1d', 'tb_ast_func_map_2d'])
        else:
            steps_to_execute = ['tb_ast', 'tb_ast_func', 'tb_ast_func_map_1d', 'tb_ast_func_map_2d']

    ps.load_environment_main()
    
    sql_var_map = {
        'tb_ast': ps.SQL_TB_AST,
        'tb_ast_func': ps.SQL_TB_AST_FUNC,
        'tb_ast_func_map_1d': ps.SQL_TB_AST_FUNC_MAP_1D,
        'tb_ast_func_map_2d': ps.SQL_TB_AST_FUNC_MAP_2D,
    }
    
    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()

    for step in steps_to_execute:
        sql_path = sql_var_map.get(step)
        if not sql_path:
            print(f"[WARN] SQL path desconhecido para step: {step}")
            continue
        sql_file_path = sql_path
        print(f"\nExecutando {step}.sql...")
        execute_sql_file(cursor, sql_file_path)

        if step == 'tb_ast_func_map_2d':
            copy_tb_ast_func_map_2d_to_painel()

        while True:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM tb_{step[3:]}")
                count = cursor.fetchone()[0]
                if count > 0:
                    break
                check_sqlite_available(sqlite_db_path)
            except sqlite3.Error:
                check_sqlite_available(sqlite_db_path)
            time.sleep(1)

    conn.commit()
    conn.close()


def select_json_to_sqlite(json_dir=None, json_type='ast', version_filter=None):
    """
    Seleciona os arquivos JSON mais recentes de ps.TARGET_DART.
    - Separa o nome do arquivo em: timestamp, file_path
    - file_path: valores unicos (distinct)
    - timestamp: mais recente para cada file_path
    Retorna lista de dicionarios com: {'timestamp': str, 'file_path': str, 'json_data': dict}
    """
    if json_dir is None:
        if json_type == 'ast':
            json_dir = ps.TARGET_DART
        elif json_type == 'raw':
            json_dir = ps.TARGET_RAW
        elif json_type == 'func':
            json_dir = ps.TARGET_DART_FUNC
        else:
            json_dir = ps.TARGET_DART

    if not os.path.isdir(json_dir):
        print(f"[ERRO] Diretorio nao encontrado: {json_dir}")
        return []

    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]
    if not json_files:
        print(f"[INFO] Nenhum arquivo JSON encontrado em: {json_dir}")
        return []

    parsed_files = []
    for filename in json_files:
        name_without_ext = filename[:-5]
        timestamp_str = None
        file_path_str = None

        parts = name_without_ext.split('_', 1)
        if len(parts) >= 2:
            timestamp_str = parts[0]
            if '^' in parts[1]:
                file_path_str = parts[1].replace('^', '/') + '.dart'
            elif parts[1].lower().endswith('.dart'):
                file_path_str = parts[1]
            else:
                file_path_str = parts[1] + '.dart'
        else:
            print(f"[WARN] Formato de nome invalido: {filename}")
            continue

        if timestamp_str and file_path_str:
            parsed_files.append({
                'timestamp': timestamp_str,
                'file_path': file_path_str,
                'filename': filename,
                'full_path': os.path.join(json_dir, filename)
            })

    if not parsed_files:
        return []

    if not version_filter or 'all' in version_filter:
        selected = parsed_files
        print(f"[VERSION_FILTER] all — {len(selected)} JSON(s)")
    else:
        selected = []
        if 'latest' in version_filter:
            latest_by_fp = {}
            for item in parsed_files:
                fp = item['file_path']
                if fp not in latest_by_fp or item['timestamp'] > latest_by_fp[fp]['timestamp']:
                    latest_by_fp[fp] = item
            selected.extend(latest_by_fp.values())
        explicit = [v for v in version_filter if v != 'latest']
        if explicit:
            for item in parsed_files:
                if item['timestamp'] in explicit:
                    selected.append(item)
        print(f"[VERSION_FILTER] {version_filter} — {len(selected)} JSON(s)")

    result = []
    for item in selected:
        try:
            with open(item['full_path'], 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            result.append({
                'timestamp': item['timestamp'],
                'file_path': item['file_path'],
                'json_data': json_data
            })
        except Exception as e:
            print(f"[ERRO] Erro ao ler {item['filename']}: {e}")

    return result


def upsert_sqlite(sqlite_db_path=None, table_name=None, version_filter=None):
    """
    Realiza upsert dos JSONs mais recentes na tabela flutter_app_ast.
    - Chama select_json_to_sqlite para obter os arquivos mais recentes
    - Faz upsert na tabela usando file_path como chave
    """
    ps.load_environment_main()
    
    if sqlite_db_path is None:
        sqlite_db_path = ps.DB_PARSE_DART if ps.DB_PARSE_DART else ''
    if table_name is None:
        table_name = ps.TB_AST
    if version_filter is None:
        version_filter = ps.TARGET_DART_VERSION_FILTER

    # Obter JSONs mais recentes
    json_list = select_json_to_sqlite(version_filter=version_filter)
    if not json_list:
        print("[INFO] Nenhum JSON para inserir/atualizar")
        return

    # Garantir que o diretório do banco existe
    os.makedirs(os.path.dirname(sqlite_db_path), exist_ok=True)

    conn = sqlite3.connect(sqlite_db_path)
    cursor = conn.cursor()

    # Verificar quais file_path já existem no banco
    try:
        cursor.execute(f"SELECT file_path FROM {table_name}")
    except sqlite3.OperationalError:
        print(f"[ERRO] Tabela '{table_name}' não existe no banco '{sqlite_db_path}'. Execute o schema SQL primeiro.")
        conn.close()
        return
    existing_file_paths = set(row[0] for row in cursor.fetchall())

    insert_count = 0
    update_count = 0

    for item in json_list:
        file_path = item['file_path']
        timestamp = item['timestamp']
        json_data_str = json.dumps(item['json_data'])
        project_name = Path(ps.PAINEL_ROOT).parent.name
        version = timestamp
        folder_path = ps.SOURCE_DART

        FlutterAppAst(
            project_name=project_name,
            version=version,
            folder_path=folder_path,
            file_path=file_path,
            json_data=json_data_str
        )

        if file_path in existing_file_paths:
            # UPDATE
            cursor.execute(f"""
                UPDATE {table_name}
                SET json_data = ?, version = ?, folder_path = ?, project_name = ?
                WHERE file_path = ?
            """, (json_data_str, version, folder_path, project_name, file_path))
            update_count += 1
        else:
            # INSERT
            cursor.execute(f"""
                INSERT INTO {table_name} (project_name, version, folder_path, file_path, json_data)
                VALUES (?, ?, ?, ?, ?)
            """, (project_name, version, folder_path, file_path, json_data_str))
            insert_count += 1
        # print(f"dados enviados para sqlite: {insert_count} inserts, {update_count} updates")

    conn.commit()
    conn.close()

    print(f"[OK] Upsert concluído: {insert_count} inserts, {update_count} updates")


def copy_tb_ast_func_map_2d_to_painel():
    """
    Sincroniza a tabela tb_ast_func_map_2d de parse_dart.db para painel_tkinter.db
    - Insere linhas novas (existem em parse_dart mas não em tkinter)
    - Remove linhas eliminadas (existem em tkinter mas não em parse_dart)
    """
    ps.load_environment_main()
    
    parse_dart_db = ps.DB_PARSE_DART
    painel_tkinter_db = ps.DB_PAINEL_TKINTER
    
    print(f"\n[SYNC] Sincronizando tb_ast_func_map_2d...")
    
    conn_source = sqlite3.connect(parse_dart_db)
    conn_target = sqlite3.connect(painel_tkinter_db)
    
    cursor_source = conn_source.cursor()
    cursor_target = conn_target.cursor()
    
    # Buscar todos os dados do source
    cursor_source.execute("""
        SELECT file_path, ClassDeclarationImpl, MethodDeclarationImpl, VariableDeclarationImpl, max_count 
        FROM tb_ast_func_map_2d
    """)
    source_rows = set(cursor_source.fetchall())
    
    # Buscar todos os dados do target
    cursor_target.execute("""
        SELECT file_path, ClassDeclarationImpl, MethodDeclarationImpl, VariableDeclarationImpl, max_count 
        FROM tb_ast_func_map_2d
    """)
    target_rows = set(cursor_target.fetchall())
    
    # Novas linhas: existem em source mas não em target
    new_rows = source_rows - target_rows
    
    # Linhas eliminadas: existem em target mas não em source
    deleted_rows = target_rows - source_rows
    
    # Inserir novas linhas
    if new_rows:
        cursor_target.executemany(
            "INSERT INTO tb_ast_func_map_2d (file_path, ClassDeclarationImpl, MethodDeclarationImpl, VariableDeclarationImpl, max_count) VALUES (?, ?, ?, ?, ?)",
            list(new_rows)
        )
        print(f"[SYNC] Inseridos {len(new_rows)} novos registros")
    
    # Remover linhas eliminadas
    if deleted_rows:
        for row in deleted_rows:
            file_path, ClassDeclarationImpl, MethodDeclarationImpl, VariableDeclarationImpl, max_count = row
            if MethodDeclarationImpl is None:
                cursor_target.execute(
                    "DELETE FROM tb_ast_func_map_2d WHERE file_path = ? AND ClassDeclarationImpl = ? AND MethodDeclarationImpl IS NULL AND VariableDeclarationImpl = ? AND max_count = ?",
                    (file_path, ClassDeclarationImpl, VariableDeclarationImpl, max_count)
                )
            else:
                cursor_target.execute(
                    "DELETE FROM tb_ast_func_map_2d WHERE file_path = ? AND ClassDeclarationImpl = ? AND MethodDeclarationImpl = ? AND VariableDeclarationImpl = ? AND max_count = ?",
                    row
                )
        print(f"[SYNC] Removidos {len(deleted_rows)} registros")
    
    conn_target.commit()
    conn_source.close()
    conn_target.close()
    
    print(f"[OK] Sincronização concluída: {len(new_rows)} novos, {len(deleted_rows)} removidos")


def from_json_upsert_tag_map():
    """
    Cria/Atualiza tabela tag_map no banco painel_tkinter a partir do JSON logs_tag_map.json.
    Schema: similar a tb_ast_func_map_2d (file_path, class, method, log_name, placeholders)
    """
    ps.load_environment_main()
    
    json_path = os.path.join(ps.TARGET_LOG_DISPLAY, 'logs_tag_map.json')
    painel_tkinter_db = ps.DB_PAINEL_TKINTER
    
    print(f"\n[UPSERT_TAG_MAP] Lendo JSON: {json_path}")
    
    if not os.path.exists(json_path):
        print(f"[ERRO] JSON não encontrado: {json_path}")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    validated = []
    for item in raw_data:
        try:
            entry = TagMapEntry.model_validate(item)
            validated.append(entry)
        except Exception as e:
            print(f'[WARN] tag_map entry validation failed: {e}, skipping')
            continue

    conn = sqlite3.connect(painel_tkinter_db)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS tag_map")
    
    cursor.execute("""
        CREATE TABLE tag_map (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_name TEXT,
            file_path TEXT,
            class_name TEXT,
            method_name TEXT,
            log_name TEXT,
            VariableDeclarationImpl TEXT
        )
    """)
    
    insert_count = 0
    for entry in validated:
        tag_name = entry.tag_name
        file_path = entry.file_path
        class_name = entry.class_name or ''
        method_name = entry.method_name or ''
        log_name = entry.log_name or ''
        placeholders_var_remove = entry.placeholders_var_remove
        
        if placeholders_var_remove is None:
            cursor.execute("""
                INSERT INTO tag_map (tag_name, file_path, class_name, method_name, log_name)
                VALUES (?, ?, ?, ?, ?)
            """, (tag_name, file_path, class_name, method_name, log_name))
            insert_count += 1
        elif isinstance(placeholders_var_remove, list):
            if not placeholders_var_remove:
                cursor.execute("""
                    INSERT INTO tag_map (tag_name, file_path, class_name, method_name, log_name)
                    VALUES (?, ?, ?, ?, ?)
                """, (tag_name, file_path, class_name, method_name, log_name))
                insert_count += 1
            else:
                for var_remove in placeholders_var_remove:
                    cursor.execute("""
                        INSERT INTO tag_map (tag_name, file_path, class_name, method_name, log_name, VariableDeclarationImpl)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (tag_name, file_path, class_name, method_name, log_name, var_remove))
                    insert_count += 1
    
    conn.commit()
    conn.close()
    
    print(f"[OK] tag_map upsert concluído: {insert_count} registros")


def from_json_upsert_logs_string():
    """
    Cria/Atualiza tabela logs_string no banco painel_tkinter a partir do JSON logs_string.json.
    Schema: achata placeholders_var - cada key vira uma linha com VariableDeclarationImpl.
    """
    ps.load_environment_main()
    
    json_path = str(ps.PAINEL_SETTINGS_DIR / 'logs_string.json')
    painel_tkinter_db = ps.DB_PAINEL_TKINTER
    
    print(f"\n[UPSERT_LOGS_STRING] Lendo JSON: {json_path}")
    
    if not os.path.exists(json_path):
        print(f"[ERRO] JSON não encontrado: {json_path}")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    validated = []
    for item in raw_data:
        try:
            entry = LogsStringEntry.model_validate(item)
            validated.append(entry)
        except Exception as e:
            print(f'[WARN] logs_string entry validation failed: {e}, skipping')
            continue

    conn = sqlite3.connect(painel_tkinter_db)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS logs_string")
    
    cursor.execute("""
        CREATE TABLE logs_string (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            log_name TEXT,
            VariableDeclarationImpl TEXT
        )
    """)
    
    insert_count = 0
    for entry in validated:
        log_name = entry.log_name
        placeholders_var = entry.placeholders_var
        
        for var_key in placeholders_var.keys():
            cursor.execute("""
                INSERT INTO logs_string (log_name, VariableDeclarationImpl)
                VALUES (?, ?)
            """, (log_name, var_key))
            insert_count += 1
    
    conn.commit()
    conn.close()
    
    print(f"[OK] logs_string upsert concluído: {insert_count} registros")


def main(action=None):
    """
    Orquestra as operações de importação SQLite.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Importação de dados SQLite')
    parser.add_argument('action', nargs='?', type=str, default=None, help='Ação a executar')
    parser.add_argument('--action', type=str, default=None, dest='action_flag', help='Ação a executar')
    args = parser.parse_args()
    
    # action pode vir de: parametro, arg posicional, ou --action
    action = action or args.action or args.action_flag
    
    # Normalizar: remover --action se vier junto
    if action and action.startswith('--action '):
        action = action.replace('--action ', '')
    
    if not action:
        parser.print_help()
        return
    
    ps.load_environment_main()
    
    if action == 'upsert':
        upsert_sqlite()
    elif action == 'triggers':
        sqlite_triggers(ps.DB_PARSE_DART, None, None)
    elif action == 'sync_ast_func_map_2d':
        copy_tb_ast_func_map_2d_to_painel()
    elif action == 'upsert_tag_map':
        from_json_upsert_tag_map()
    elif action == 'upsert_logs_string':
        from_json_upsert_logs_string()
    else:
        print(f"[ERRO] Action desconhecida: {action}")


if __name__ == "__main__":
    main()

