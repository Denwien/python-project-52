"""
Pytest plugin that blocks conflicting plugins early in the loading process.
This plugin must be loaded BEFORE pytest-env and pytest-dotenv.
"""
import sys
import os

os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

# Apply monkey-patch to pluggy BEFORE pytest loads other plugins
def _apply_patch():
    try:
        import pluggy
    except ImportError:
        return
    
    if hasattr(pluggy.PluginManager, '_pytest_plugin_blocker_patched'):
        return
    
    _original_load_setuptools_entrypoints = pluggy.PluginManager.load_setuptools_entrypoints
    
    def _patched_load_setuptools_entrypoints(self, name):
        if name == "pytest11":
            from importlib.metadata import entry_points
            try:
                eps = entry_points(group=name)
            except TypeError:
                eps = entry_points().get(name, [])
            filtered_eps = []
            for ep in eps:
                ep_name_lower = ep.name.lower()
                if ("pytest_dotenv" not in ep_name_lower and 
                    "pytest-dotenv" not in ep_name_lower and
                    "pytest_env" not in ep_name_lower and
                    "pytest-env" not in ep_name_lower):
                    filtered_eps.append(ep)
            
            for ep in filtered_eps:
                try:
                    plugin = ep.load()
                    self.register(plugin, name=ep.name)
                except Exception:
                    pass
        else:
            return _original_load_setuptools_entrypoints(self, name)
    
    pluggy.PluginManager.load_setuptools_entrypoints = _patched_load_setuptools_entrypoints
    pluggy.PluginManager._pytest_plugin_blocker_patched = True

# Apply patch immediately when module is imported
_apply_patch()

def pytest_load_initial_conftests(early_config, parser, args):
    """Block plugins before they can register options."""
    try:
        early_config.pluginmanager.set_blocked("pytest_dotenv")
        early_config.pluginmanager.set_blocked("pytest-dotenv")
        early_config.pluginmanager.set_blocked("pytest_env")
        early_config.pluginmanager.set_blocked("pytest-env")
    except Exception:
        pass

def pytest_addoption(parser, pluginmanager):
    """Block plugins during option registration."""
    try:
        pluginmanager.set_blocked("pytest_dotenv")
        pluginmanager.set_blocked("pytest-dotenv")
        pluginmanager.set_blocked("pytest_env")
        pluginmanager.set_blocked("pytest-env")
    except Exception:
        pass
