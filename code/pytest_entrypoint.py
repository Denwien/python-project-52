import sys
import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

code_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(code_dir)

if code_dir not in sys.path:
    sys.path.insert(0, code_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from code import pytest_plugin_blocker
except ImportError:
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass

import pytest

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    sys.exit(pytest.main(args))
