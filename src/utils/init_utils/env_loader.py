import os
import sys
import json
from pathlib import Path
from typing import Dict, Any

PAINEL_SETTINGS_DIR = Path(__file__).parent
PAINEL_SRC_DIR      = PAINEL_SETTINGS_DIR.parent.parent
PAINEL_SERVICES_DIR     = PAINEL_SRC_DIR / 'services'
PAINEL_PARSE_DIR        = PAINEL_SERVICES_DIR / 'parse'
PAINEL_LOGS_DIR         = PAINEL_SERVICES_DIR / 'logs'
PAINEL_DART_TOOLS_DIR   = PAINEL_SRC_DIR / 'services' / 'dart_tools'
PAINEL_TKINTER_DIR      = PAINEL_SRC_DIR / 'tkinter'

SQL_SRC_DIR         = PAINEL_SRC_DIR / 'sql_sqlite'
SQL_PARSE_MD_DIR    = SQL_SRC_DIR / 'sql_parse_md'
SQL_PARSE_SCRIPT_DIR= SQL_SRC_DIR / 'sql_parse_script'
SQL_TKINTER_DIR     = SQL_SRC_DIR / 'sql_tkinter'

ENV_PAINEL_JSON     = PAINEL_SRC_DIR / 'config' / 'set_painel_pipeline_paths.json'
ACTIONS_DATA_JSON   = PAINEL_SRC_DIR / 'config' / 'set_painel_actions_data_paths.json'
MENU_JSON           = PAINEL_SRC_DIR / 'config' / 'set_painel_menu.json'

PAINEL_ROOT = ''
ABS_PATH_DART_EXECUTABLE = ''
ABS_PATH_DART_SDK = ''

_env_loaded = False


def load_env_file(env_file_path: str) -> Dict[str, str]:
    env_vars = {}
    if not os.path.exists(env_file_path):
        return env_vars
    with open(env_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip().strip('"').strip("'")
    return env_vars


def load_env_base() -> Dict[str, str]:
    env_base = r"C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\.env.base"
    env_vars = load_env_file(env_base)
    if 'ENV_PAINEL' in env_vars:
        os.environ['ENV_PAINEL'] = env_vars['ENV_PAINEL']
    return env_vars


def _save_absolute_paths(json_path: Path, absolute_dict: dict) -> None:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['absolute_paths'] = absolute_dict
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_painel_pipeline_paths() -> None:
    global PAINEL_ROOT, ABS_PATH_DART_EXECUTABLE, ABS_PATH_DART_SDK

    env_painel = os.environ.get('ENV_PAINEL', '')
    if not env_painel:
        raise ValueError("ENV_PAINEL nao encontrado no ambiente. Execute o PS1 primeiro ou configure ENV_PAINEL.")

    pipeline_path = Path(env_painel)
    if not pipeline_path.exists():
        raise FileNotFoundError(f"set_painel_pipeline_paths.json nao encontrado em: {pipeline_path}")

    with open(pipeline_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    PAINEL_ROOT = str(PAINEL_SETTINGS_DIR.parent.parent.parent.resolve())
    tool_paths = data.get('tool_paths', {})
    ABS_PATH_DART_EXECUTABLE = tool_paths.get('ABS_PATH_DART_EXECUTABLE', '')
    ABS_PATH_DART_SDK = tool_paths.get('ABS_PATH_DART_SDK', '')

    absolute = {
        'PAINEL_ROOT': str(PAINEL_ROOT),
        'tool_paths': dict(tool_paths)
    }
    _save_absolute_paths(pipeline_path, absolute)


def load_environment_main() -> None:
    global _env_loaded
    if _env_loaded:
        return

    _src = str(PAINEL_SRC_DIR.resolve())
    if _src not in sys.path:
        sys.path.insert(0, _src)

    load_env_base()
    load_painel_pipeline_paths()

    from utils.io_utils.config_io import load_painel_actions_data_paths
    load_painel_actions_data_paths()

    _env_loaded = True
