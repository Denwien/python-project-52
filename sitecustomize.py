import sys
import os

if 'pytest' in ' '.join(sys.argv) or any('pytest' in arg for arg in sys.argv):
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass
