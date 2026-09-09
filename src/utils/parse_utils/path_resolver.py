from pathlib import Path

from utils.init_utils import env_loader


def resolve_data_paths(data: dict) -> dict:
    root = Path(env_loader.PAINEL_ROOT).resolve()
    resolved = {}
    for key, value in data.items():
        if isinstance(value, str):
            resolved[key] = str((root / value).resolve())
        elif isinstance(value, dict):
            if 'paths' in value:
                new_val = dict(value)
                new_val['paths'] = [str((root / p).resolve()) for p in value.get('paths', [])]
                resolved[key] = new_val
            elif 'path' in value:
                new_val = dict(value)
                new_val['path'] = str((root / value['path']).resolve())
                resolved[key] = new_val
            else:
                resolved[key] = resolve_data_paths(value)
        else:
            resolved[key] = value
    return resolved
