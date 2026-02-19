#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

import pytest_plugin_blocker
import pytest

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-vv", "tests"]
    sys.exit(pytest.main(["-p", "no:pytest_dotenv", "-p", "no:pytest-dotenv"] + args))
