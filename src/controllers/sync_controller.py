from pathlib import Path

from utils.init_utils import env_loader
from utils.io_utils import config_io


def sync_json_to_sqlite(source_type: str = 'dart'):
    env_loader.load_environment_main()
    from utils.io_utils.painel_sqlite_import import upsert_sqlite
    db_path = config_io.DB_PARSE_DART if source_type == 'dart' else config_io.DB_PARSE_MD
    table_name = config_io.TB_AST if source_type == 'dart' else config_io.TB_MD_BLOCKS
    upsert_sqlite(sqlite_db_path=db_path, table_name=table_name)


def sync_triggers(action: str = 'ast'):
    env_loader.load_environment_main()
    from utils.io_utils.painel_sqlite_import import sqlite_triggers
    db_path = config_io.DB_PARSE_DART
    sqlite_triggers(sqlite_db_path=db_path, action=action)
