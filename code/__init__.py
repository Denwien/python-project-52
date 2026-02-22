import os
import sys

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

try:
    from . import pytest_plugin_blocker
except ImportError:
    pass
