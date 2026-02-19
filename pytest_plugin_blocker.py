import pluggy

_original_load_setuptools_entrypoints = pluggy.PluginManager.load_setuptools_entrypoints

def _patched_load_setuptools_entrypoints(self, name):
    if name == "pytest11":
        from importlib.metadata import entry_points
        try:
            eps = entry_points(group=name)
        except TypeError:
            eps = entry_points().get(name, [])
        for ep in eps:
            ep_name_lower = ep.name.lower()
            if "pytest_dotenv" not in ep_name_lower and "pytest-dotenv" not in ep_name_lower:
                try:
                    plugin = ep.load()
                    self.register(plugin, name=ep.name)
                except Exception:
                    pass
    else:
        return _original_load_setuptools_entrypoints(self, name)

pluggy.PluginManager.load_setuptools_entrypoints = _patched_load_setuptools_entrypoints
