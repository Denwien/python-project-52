def pytest_configure(config):
    try:
        config.pluginmanager.set_blocked("pytest_dotenv")
    except Exception:
        pass
