def pytest_load_initial_conftests(early_config, parser, args):
    try:
        early_config.pluginmanager.set_blocked("pytest_dotenv")
        early_config.pluginmanager.set_blocked("pytest-dotenv")
        early_config.pluginmanager.set_blocked("pytest_env")
        early_config.pluginmanager.set_blocked("pytest-env")
    except Exception:
        pass

def pytest_addoption(parser, pluginmanager):
    try:
        pluginmanager.set_blocked("pytest_dotenv")
        pluginmanager.set_blocked("pytest-dotenv")
        pluginmanager.set_blocked("pytest_env")
        pluginmanager.set_blocked("pytest-env")
    except Exception:
        pass
