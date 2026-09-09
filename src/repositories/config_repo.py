import json
from pathlib import Path
from typing import Dict, Any, Optional

from utils.init_utils.env_loader import PAINEL_SRC_DIR, ENV_PAINEL_JSON, ACTIONS_DATA_JSON, MENU_JSON, PAINEL_ROOT


def get_pipeline_paths() -> Dict[str, Any]:
    if not ENV_PAINEL_JSON.exists():
        return {}
    with open(ENV_PAINEL_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_actions_data_paths() -> Dict[str, Any]:
    if not ACTIONS_DATA_JSON.exists():
        return {}
    with open(ACTIONS_DATA_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_menu() -> Dict[str, Any]:
    if not MENU_JSON.exists():
        return {}
    with open(MENU_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(file_path: Path, data: Dict[str, Any]) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
