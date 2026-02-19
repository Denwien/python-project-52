import sys

def pytest_load_initial_conftests(early_config, parser, args):
    try:
        early_config.pluginmanager.set_blocked("pytest_dotenv")
    except Exception:
        pass
