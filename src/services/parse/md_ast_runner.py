import sys
import argparse
from pathlib import Path

_src = str((Path(__file__).parent.parent.parent).resolve())
_init_utils = str((Path(__file__).parent.parent.parent / 'utils' / 'init_utils').resolve())
_io_utils = str((Path(__file__).parent.parent.parent / 'utils' / 'io_utils').resolve())
_models = str((Path(__file__).parent.parent.parent / 'models').resolve())
for p in [_init_utils, _io_utils, _models]:
    if p not in sys.path: sys.path.insert(0, p)
import painel_settings as ps
import md_ast_io
import md_ast_persistence
from md_ast_parser import GenerateAst


class MdAstRunner:
    def __init__(self):
        self.args = None
        self.env_loaded = False

    def load_environment(self):
        ps.load_environment_main()
        self.env_loaded = True

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Parser AST de arquivos Markdown')
        parser.add_argument('--action', required=True,
                            choices=['md_ast', 'md_json', 'md_sqlite'],
                            help='Acao a executar')
        parser.add_argument('--input', nargs='*', default=None,
                            help='Paths de entrada (arquivos ou diretorios)')
        self.args = parser.parse_args()
        return self.args

    def dispatch(self, action, args):
        source_config = ps.SOURCE_MD_CONFIG

        if action in ('md_ast', 'md_json'):
            reader = md_ast_io.ReadInputFiles()
            input_paths = args.input or source_config.get('paths', [ps.SOURCE_MD]) if source_config else [ps.SOURCE_MD]
            files = reader.scan(input_paths, source_config=source_config)

            generator = GenerateAst()
            ast_model = generator.get_ast_model()
            entries = []
            for md_file in files:
                ast = generator.parse_file(md_file, ast_model)
                entry = generator.build_entry(
                    md_file, ast,
                    reader._get_project_name(),
                    reader._get_session_version(),
                    ps.PAINEL_ROOT
                )
                entries.append(entry)

            output_dir = ps.TARGET_MD
            db_path = ps.DB_PARSE_MD

            saver = md_ast_persistence.SaveOutputFiles()
            schemas = {
                'blocks': md_ast_persistence.json_schema_blocks,
                'code': md_ast_persistence.json_schema_code,
                'tables': md_ast_persistence.json_schema_tables,
            }

            if action == 'md_ast':
                saver.save_all(entries, schemas, output_dir, db_path)
            else:
                for entry in entries:
                    for suffix, schema in schemas.items():
                        data = saver._extract(entry, schema)
                        if not data:
                            continue
                        saver.save_json(data, suffix, entry, output_dir)

        elif action == 'md_sqlite':
            from painel_sqlite_import import upsert_sqlite
            upsert_sqlite(sqlite_db_path=ps.DB_PARSE_MD, version_filter=ps.TARGET_MD_VERSION_FILTER)
            saver = md_ast_persistence.SaveOutputFiles()
            saver.create_views(ps.DB_PARSE_MD)

    def run(self):
        self.load_environment()
        self.parse_args()
        self.dispatch(self.args.action, self.args)


if __name__ == '__main__':
    app = MdAstRunner()
    app.run()
