import sys

pytest_plugins = []

for plugin in list(sys.modules.keys()):
    if "pytest_dotenv" in plugin:
        if "pytest_dotenv" in sys.modules:
            del sys.modules["pytest_dotenv"]
