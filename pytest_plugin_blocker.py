import sys
import pluggy

_original_load_setuptools_entrypoints = pluggy.PluginManager.load_setuptools_entrypoints

def _patched_load_setuptools_entrypoints(self, name):
    if name == "pytest11":
        plugins = []
        for ep in self._iter_plugin_distinfo():
            if "pytest_dotenv" not in ep.name.lower() and "pytest-dotenv" not in ep.name.lower():
                plugins.append(ep)
        for ep in plugins:
            try:
                plugin = ep.load()
                self.register(plugin, name=ep.name)
            except Exception:
                pass
    else:
        return _original_load_setuptools_entrypoints(self, name)

pluggy.PluginManager.load_setuptools_entrypoints = _patched_load_setuptools_entrypoints
