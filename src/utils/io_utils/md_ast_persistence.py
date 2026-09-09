import os
import sys
import json
import sqlite3
from pathlib import Path
from datetime import datetime

_init_utils = str((Path(__file__).parent.parent / 'init_utils').resolve())
_io_utils = str(Path(__file__).parent.resolve())
_parse_utils = str((Path(__file__).parent.parent / 'parse_utils').resolve())
_models = str((Path(__file__).parent.parent.parent / 'models').resolve())
for p in [_init_utils, _io_utils, _parse_utils, _models]:
    if p not in sys.path: sys.path.insert(0, p)
import parse_export
import string_utils
import painel_settings as ps
from ast_md_model import MdBlockRow, MdCodeRow, MdTableRow


class SaveOutputFiles:
    def _extract(self, entry, schema):
        ast = entry.get('ast', {})
        results = []
        field_defs = {f['name']: f for f in schema.get('fields', [])}

        blocks = ast.get('children', [])

        if schema['type'] == 'blocks':
            for blk in blocks:
                row = {}
                for name, fd in field_defs.items():
                    if fd.get('source') == 'entry':
                        row[name] = entry.get(name, '')
                    elif fd.get('source', '').startswith('ast.node.'):
                        field_key = fd['source'].split('.')[-1]
                        row[name] = blk.get(field_key, fd.get('default', ''))
                    elif fd.get('source') == 'ast' and fd.get('method') == 'collect_text':
                        row[name] = self._collect_text(blk.get('children', []))
                results.append(row)

        elif schema['type'] == 'code':
            for blk in blocks:
                if blk.get('type') != 'code':
                    continue
                row = {}
                for name, fd in field_defs.items():
                    if fd.get('source') == 'entry':
                        row[name] = entry.get(name, '')
                    elif fd.get('source', '').startswith('ast.node.'):
                        field_key = fd['source'].split('.')[-1]
                        row[name] = blk.get(field_key, fd.get('default', ''))
                results.append(row)

        elif schema['type'] == 'tables':
            for blk in blocks:
                if blk.get('type') != 'table':
                    continue
                for ri, table_row in enumerate(blk.get('children', [])):
                    if table_row.get('type') != 'tableRow':
                        continue
                    for ci, cell in enumerate(table_row.get('children', [])):
                        row = {}
                        for name, fd in field_defs.items():
                            if fd.get('source') == 'entry':
                                row[name] = entry.get(name, '')
                            elif fd.get('source', '').startswith('ast.node.'):
                                field_key = fd['source'].split('.')[-1]
                                row[name] = blk.get(field_key, fd.get('default', ''))
                            elif name == 'row_index':
                                row[name] = ri
                            elif name == 'cell_index':
                                row[name] = ci
                            elif name == 'cell_type':
                                row[name] = cell.get('type', 'tableCell')
                            elif name == 'value':
                                row[name] = self._collect_text(cell.get('children', []))
                        results.append(row)
        return results

    def _collect_text(self, children):
        return string_utils.collect_text(children)

    def save_json(self, data, suffix, entry, output_dir):
        project_name = entry.get('project_name', 'unknown')
        version = entry.get('version', datetime.now().isoformat())
        file_path = entry.get('file_path', 'unknown.md')

        timestamp = version.replace(':', '').replace('-', '').replace('.', '')
        child_path = str(Path(file_path).parent).replace('\\', '^').replace('/', '^')
        file_stem = Path(file_path).stem
        filename = f"{timestamp}_{child_path}^{file_stem}.{suffix}.json"

        output_path = Path(output_dir) / filename
        os.makedirs(output_path.parent, exist_ok=True)
        parse_export.write_to_json(data, str(output_path))

    def save_sqlite(self, data, table_name, entry, db_path):
        db_path = Path(db_path)
        os.makedirs(db_path.parent, exist_ok=True)

        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_name TEXT,
                version TEXT,
                folder_path TEXT,
                file_path TEXT UNIQUE,
                json_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        json_str = json.dumps(data, ensure_ascii=False)

        cursor.execute(f"SELECT file_path FROM {table_name} WHERE file_path = ?",
                       (entry['file_path'],))
        exists = cursor.fetchone()

        if exists:
            cursor.execute(f"""
                UPDATE {table_name}
                SET json_data = ?, version = ?, project_name = ?, folder_path = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE file_path = ?
            """, (json_str, entry['version'], entry['project_name'],
                  entry['folder_path'], entry['file_path']))
        else:
            cursor.execute(f"""
                INSERT INTO {table_name}
                    (project_name, version, folder_path, file_path, json_data)
                VALUES (?, ?, ?, ?, ?)
            """, (entry['project_name'], entry['version'],
                  entry['folder_path'], entry['file_path'], json_str))

        conn.commit()
        conn.close()

    def create_views(self, db_path):
        views_dir = ps.SQL_PARSE_MD_DIR
        if not os.path.isdir(views_dir):
            return
        conn = sqlite3.connect(str(db_path))
        for fname in sorted(os.listdir(views_dir)):
            if not fname.startswith('vw_') or not fname.endswith('.sql'):
                continue
            fpath = os.path.join(views_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
        conn.commit()
        conn.close()

    def save_all(self, entries, schemas, output_dir, db_path):
        for entry in entries:
            for suffix, schema in schemas.items():
                data = self._extract(entry, schema)
                if not data:
                    continue
                model_map = {'blocks': MdBlockRow, 'code': MdCodeRow, 'tables': MdTableRow}
                model_class = model_map.get(suffix)
                if model_class:
                    data = [r.model_dump() for r in parse_export.validate_to_model(data, model_class)]
                self.save_json(data, suffix, entry, output_dir)
                self.save_sqlite(data,
                                 schema.get('table_name', f'tb_json_md_ast_{suffix}'),
                                 entry, db_path)
        self.create_views(db_path)


def load_schema(name):
    _SCHEMA_DIR = Path(__file__).parent.parent.parent / 'models' / 'schemas'
    path = _SCHEMA_DIR / f'schema_md_{name}.json'
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    print(f'[WARN] Schema file not found: {path}, using inline fallback')
    return _INLINE_SCHEMAS[name]


_INLINE_SCHEMAS = {
    'blocks': {
        "type": "blocks",
        "table_name": "tb_json_md_ast_blocks",
        "fields": [
            {"name": "file_path", "source": "entry"},
            {"name": "start_line", "source": "ast.node.start_line"},
            {"name": "type", "source": "ast.node.type"},
            {"name": "depth", "source": "ast.node.depth", "default": 0},
            {"name": "h1", "source": "ast.node.h1", "default": ""},
            {"name": "h2", "source": "ast.node.h2", "default": ""},
            {"name": "h3", "source": "ast.node.h3", "default": ""},
            {"name": "h4", "source": "ast.node.h4", "default": ""},
            {"name": "h5", "source": "ast.node.h5", "default": ""},
            {"name": "h6", "source": "ast.node.h6", "default": ""},
            {"name": "value", "source": "ast", "method": "collect_text"},
        ]
    },
    'code': {
        "type": "code",
        "table_name": "tb_json_md_ast_code",
        "fields": [
            {"name": "file_path", "source": "entry"},
            {"name": "start_line", "source": "ast.node.start_line"},
            {"name": "type", "source": "ast.node.type"},
            {"name": "depth", "source": "ast.node.depth", "default": 0},
            {"name": "h1", "source": "ast.node.h1", "default": ""},
            {"name": "h2", "source": "ast.node.h2", "default": ""},
            {"name": "h3", "source": "ast.node.h3", "default": ""},
            {"name": "h4", "source": "ast.node.h4", "default": ""},
            {"name": "h5", "source": "ast.node.h5", "default": ""},
            {"name": "h6", "source": "ast.node.h6", "default": ""},
            {"name": "lang", "source": "ast.node.lang"},
            {"name": "value", "source": "ast.node.value"},
        ]
    },
    'tables': {
        "type": "tables",
        "table_name": "tb_json_md_ast_tables",
        "fields": [
            {"name": "file_path", "source": "entry"},
            {"name": "start_line", "source": "ast.node.start_line"},
            {"name": "type", "source": "ast.node.type"},
            {"name": "depth", "source": "ast.node.depth", "default": 0},
            {"name": "row_index", "source": "ast.row_index"},
            {"name": "cell_index", "source": "ast.cell_index"},
            {"name": "cell_type", "source": "ast.cell.type"},
            {"name": "h1", "source": "ast.node.h1", "default": ""},
            {"name": "h2", "source": "ast.node.h2", "default": ""},
            {"name": "h3", "source": "ast.node.h3", "default": ""},
            {"name": "h4", "source": "ast.node.h4", "default": ""},
            {"name": "h5", "source": "ast.node.h5", "default": ""},
            {"name": "h6", "source": "ast.node.h6", "default": ""},
            {"name": "value", "source": "ast", "method": "collect_text"},
        ]
    }
}

json_schema_blocks = load_schema('blocks')
json_schema_code = load_schema('code')
json_schema_tables = load_schema('tables')
