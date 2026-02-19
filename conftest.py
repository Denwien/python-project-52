import os
import sys

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

def pytest_configure(config):
    try:
        config.pluginmanager.set_blocked("pytest_dotenv")
    except Exception:
        pass
