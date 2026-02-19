import pytest_plugin_blocker

def pytest_configure(config):
    try:
        config.pluginmanager.set_blocked("pytest_dotenv")
        config.pluginmanager.set_blocked("pytest-dotenv")
    except Exception:
        pass
