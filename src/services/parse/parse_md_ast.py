import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.resolve()))
from md_ast_runner import MdAstRunner

if __name__ == '__main__':
    app = MdAstRunner()
    app.run()
