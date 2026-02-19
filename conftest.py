"""
Root conftest.py that applies plugin blocker patch before pytest loads plugins.
"""
import sys
import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

# Add code directory to path
code_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "code")
if code_dir not in sys.path:
    sys.path.insert(0, code_dir)

# Import and apply plugin blocker patch BEFORE pytest loads plugins
try:
    from code import pytest_plugin_blocker
except ImportError:
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass

# Also try to import early blocker
try:
    from code import pytest_early_blocker
except ImportError:
    pass
