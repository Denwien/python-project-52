import sys
import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

code_dir = os.path.dirname(os.path.abspath(__file__))
if code_dir not in sys.path:
    sys.path.insert(0, code_dir)

parent_dir = os.path.dirname(code_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from code import pytest_plugin_blocker
except ImportError:
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass

def pytest_load_initial_conftests(early_config, parser, args):
    try:
        early_config.pluginmanager.set_blocked("pytest_dotenv")
        early_config.pluginmanager.set_blocked("pytest-dotenv")
        early_config.pluginmanager.set_blocked("pytest_env")
        early_config.pluginmanager.set_blocked("pytest-env")
    except Exception:
        pass

def pytest_configure(config):
    try:
        config.pluginmanager.set_blocked("pytest_dotenv")
        config.pluginmanager.set_blocked("pytest-dotenv")
        config.pluginmanager.set_blocked("pytest_env")
        config.pluginmanager.set_blocked("pytest-env")
    except Exception:
        pass
