import sys
import pluggy

_original_register = pluggy.PluginManager.register

def _patched_register(self, plugin, name=None):
    if name and "pytest_dotenv" in name.lower():
        return None
    if hasattr(plugin, "__name__") and "pytest_dotenv" in plugin.__name__.lower():
        return None
    return _original_register(self, plugin, name)

pluggy.PluginManager.register = _patched_register
