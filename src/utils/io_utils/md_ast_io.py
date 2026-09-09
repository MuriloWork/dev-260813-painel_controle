import os
import sys
from pathlib import Path
from datetime import datetime

_init_utils = str((Path(__file__).parent.parent / 'init_utils').resolve())
_io_utils = str(Path(__file__).parent.resolve())
if _init_utils not in sys.path: sys.path.insert(0, _init_utils)
if _io_utils not in sys.path: sys.path.insert(0, _io_utils)
import parse_utils
import painel_settings as ps


class ReadInputFiles:
    def scan(self, paths, source_config=None):
        file_infos = parse_utils.get_files_from_paths(
            paths,
            extensions=('.md',),
            include_child_paths=source_config.get('include_child_paths') if source_config else None,
            include_child_globs=source_config.get('include_child_globs') if source_config else None,
            exclude_child_paths=source_config.get('exclude_child_paths') if source_config else None,
            exclude_child_globs=source_config.get('exclude_child_globs') if source_config else None,
        )
        md_files = [Path(fi['filepath']) for fi in file_infos]
        print(f"[INFO] Encontrados {len(md_files)} arquivos .md")
        return md_files

    def _get_project_name(self):
        return Path(ps.PAINEL_ROOT).parent.name

    def _get_session_version(self):
        return datetime.now().isoformat()
