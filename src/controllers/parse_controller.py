from pathlib import Path

from utils.init_utils import env_loader
from utils.io_utils import config_io


def run_md_ast(action: str = 'md_ast', input_paths=None):
    env_loader.load_environment_main()
    from services.parse import md_ast_runner
    runner = md_ast_runner.MdAstRunner()
    runner.load_environment()

    class Args:
        def __init__(self, action, input_paths):
            self.action = action
            self.input = input_paths

    args = Args(action, input_paths)
    runner.dispatch(action, args)


def run_dart_ast(action: str = 'ast'):
    env_loader.load_environment_main()
    from services.parse.parse_script_dart_ast import main as dart_main
    dart_main()


def run_raw(action: str = 'raw'):
    env_loader.load_environment_main()
    from services.parse.parse_script_raw import main as raw_main
    raw_main()
