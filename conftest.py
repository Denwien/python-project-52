import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

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
