import sys
import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

try:
    from . import pytest_plugin_blocker
except ImportError:
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass
