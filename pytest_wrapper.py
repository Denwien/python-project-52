#!/usr/bin/env python
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")
os.environ.setdefault("PYTHONSTARTUP", os.path.join(project_root, "pytest_plugin_blocker.py"))

try:
    import pytest_plugin_blocker
except ImportError:
    pass

import pytest

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-vv", "tests"]
    sys.exit(pytest.main(["-p", "no:pytest_dotenv", "-p", "no:pytest-dotenv", "-p", "no:pytest_env", "-p", "no:pytest-env"] + args))
