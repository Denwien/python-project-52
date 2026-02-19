import sys
import os

if any('pytest' in arg for arg in sys.argv):
    project_root = os.path.dirname(os.path.abspath(__file__))
    code_dir = os.path.join(project_root, 'code')
    
    if code_dir not in sys.path:
        sys.path.insert(0, code_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")
    
    try:
        from code import pytest_plugin_blocker
    except ImportError:
        try:
            import pytest_plugin_blocker
        except ImportError:
            pass
