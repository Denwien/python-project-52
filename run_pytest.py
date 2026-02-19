#!/usr/bin/env python
import sys
import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

import pytest_plugin_blocker
import pytest

if __name__ == "__main__":
    sys.exit(pytest.main(["-vv", "tests", "-p", "no:pytest_dotenv", "-p", "no:pytest-dotenv"] + sys.argv[1:]))
