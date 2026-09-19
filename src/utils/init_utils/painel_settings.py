import sys
from pathlib import Path

_src = Path(__file__).resolve().parent.parent.parent
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from utils.init_utils import env_loader
from utils.io_utils import config_io
from utils.parse_utils.path_resolver import resolve_data_paths


def __getattr__(name):
    for mod in (env_loader, config_io):
        if hasattr(mod, name):
            return getattr(mod, name)
    raise AttributeError(f"module 'painel_settings' has no attribute '{name}'")
