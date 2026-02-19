import sys
import os

if any('pytest' in arg for arg in sys.argv):
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass
