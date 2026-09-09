import json
from pathlib import Path
from typing import Dict, Any, Optional

from utils.init_utils import env_loader
from utils.parse_utils.path_resolver import resolve_data_paths

_actions_config: Dict[str, Any] = {}

DB_PARSE_DART = ''
DB_PARSE_MD = ''
DB_PAINEL_TKINTER = ''

SOURCE_DART = ''
SOURCE_RAW = ''
SOURCE_MD = ''

TARGET_LOG_DISPLAY = ''
TARGET_LOG_SESSION = ''
TARGET_MD = ''
TARGET_DART = ''
TARGET_DART_FUNC = ''
TARGET_RAW = ''

TB_AST = ''
TB_RAW = ''
TB_MD_BLOCKS = ''
TB_MD_CODE = ''
TB_MD_TABLES = ''

SQL_TB_AST = ''
SQL_TB_AST_FUNC = ''
SQL_TB_AST_FUNC_MAP_1D = ''
SQL_TB_AST_FUNC_MAP_2D = ''
SQL_MD_CODE = ''
SQL_MD_TABLES = ''

SOURCE_DART_CONFIG: Optional[dict] = None
SOURCE_RAW_CONFIG: Optional[dict] = None
SOURCE_MD_CONFIG: Optional[dict] = None

TARGET_DART_VERSION_FILTER: list = ['all']
TARGET_RAW_VERSION_FILTER: list = ['all']
TARGET_MD_VERSION_FILTER: list = ['all']
TARGET_DART_FUNC_VERSION_FILTER: list = ['all']


def load_painel_actions_data_paths() -> None:
    global _actions_config
    global DB_PARSE_DART, DB_PARSE_MD, DB_PAINEL_TKINTER
    global SOURCE_DART, SOURCE_RAW, SOURCE_MD
    global SOURCE_DART_CONFIG, SOURCE_RAW_CONFIG, SOURCE_MD_CONFIG
    global TARGET_LOG_DISPLAY, TARGET_LOG_SESSION
    global TARGET_MD, TARGET_DART, TARGET_DART_FUNC, TARGET_RAW
    global TARGET_DART_VERSION_FILTER, TARGET_RAW_VERSION_FILTER
    global TARGET_MD_VERSION_FILTER, TARGET_DART_FUNC_VERSION_FILTER
    global TB_AST, TB_RAW, TB_MD_BLOCKS, TB_MD_CODE, TB_MD_TABLES
    global SQL_TB_AST, SQL_TB_AST_FUNC, SQL_TB_AST_FUNC_MAP_1D
    global SQL_TB_AST_FUNC_MAP_2D, SQL_MD_CODE, SQL_MD_TABLES

    if not env_loader.ACTIONS_DATA_JSON.exists():
        print(f"[WARN] {env_loader.ACTIONS_DATA_JSON} nao encontrado. Usando fallback vazio.")
        return

    with open(env_loader.ACTIONS_DATA_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    dp = data.get('data_paths', {})

    raw_dp = {}
    for section in ('database', 'sources', 'targets'):
        for key, value in dp.get(section, {}).items():
            raw_dp[key] = value

    resolved_dp = resolve_data_paths(raw_dp)

    DB_PARSE_DART = resolved_dp.get('DB_PARSE_DART', '')
    DB_PARSE_MD = resolved_dp.get('DB_PARSE_MD', '')
    DB_PAINEL_TKINTER = resolved_dp.get('DB_PAINEL_TKINTER', '')

    def _resolve_source(key):
        val = resolved_dp.get(key, '')
        if isinstance(val, dict):
            return val['paths'][0] if val.get('paths') else '', val
        return val, None

    SOURCE_DART, SOURCE_DART_CONFIG = _resolve_source('SOURCE_DART')
    SOURCE_RAW, SOURCE_RAW_CONFIG = _resolve_source('SOURCE_RAW')
    SOURCE_MD, SOURCE_MD_CONFIG = _resolve_source('SOURCE_MD')

    def _resolve_target(key):
        val = resolved_dp.get(key, '')
        if isinstance(val, dict):
            return val.get('path', ''), val.get('version_filter', ['all'])
        return val, ['all']

    TARGET_LOG_DISPLAY = resolved_dp.get('TARGET_LOG_DISPLAY', '')
    TARGET_LOG_SESSION = resolved_dp.get('TARGET_LOG_SESSION', '')
    TARGET_MD, TARGET_MD_VERSION_FILTER = _resolve_target('TARGET_MD')
    TARGET_DART, TARGET_DART_VERSION_FILTER = _resolve_target('TARGET_DART')
    TARGET_DART_FUNC, TARGET_DART_FUNC_VERSION_FILTER = _resolve_target('TARGET_DART_FUNC')
    TARGET_RAW, TARGET_RAW_VERSION_FILTER = _resolve_target('TARGET_RAW')

    st = data.get('sqlite_tables', {})
    TB_AST = st.get('parse_dart', {}).get('TB_AST', '')
    TB_RAW = st.get('parse_dart', {}).get('TB_RAW', '')
    TB_MD_BLOCKS = st.get('parse_md', {}).get('TB_MD_BLOCKS', '')
    TB_MD_CODE = st.get('parse_md', {}).get('TB_MD_CODE', '')
    TB_MD_TABLES = st.get('parse_md', {}).get('TB_MD_TABLES', '')

    sp = data.get('sql_paths', {})
    resolved_sp = resolve_data_paths(sp)
    SQL_TB_AST = resolved_sp.get('SQL_TB_AST', '')
    SQL_TB_AST_FUNC = resolved_sp.get('SQL_TB_AST_FUNC', '')
    SQL_TB_AST_FUNC_MAP_1D = resolved_sp.get('SQL_TB_AST_FUNC_MAP_1D', '')
    SQL_TB_AST_FUNC_MAP_2D = resolved_sp.get('SQL_TB_AST_FUNC_MAP_2D', '')
    SQL_MD_CODE = resolved_sp.get('SQL_MD_CODE', '')
    SQL_MD_TABLES = resolved_sp.get('SQL_MD_TABLES', '')

    _actions_config = data.get('actions', {})

    absolute = {
        'data_paths': resolve_data_paths(data.get('data_paths', {})),
        'sql_paths': resolve_data_paths(data.get('sql_paths', {})),
    }
    env_loader._save_absolute_paths(env_loader.ACTIONS_DATA_JSON, absolute)


def get_action_config(script_name: str, action: str) -> Optional[dict]:
    script_actions = _actions_config.get(script_name, [])
    for cfg in script_actions:
        if cfg.get('action') == action:
            return cfg
    return None


def load_menu_targets() -> Dict[str, Any]:
    if not env_loader.MENU_JSON.exists():
        return {}
    with open(env_loader.MENU_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)
