import sys
import os

if 'pytest' in sys.modules or 'pytest' in ' '.join(sys.argv):
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass
else:
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass
