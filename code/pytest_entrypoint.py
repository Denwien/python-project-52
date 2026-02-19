#!/usr/bin/env python
"""
Pytest entry point wrapper that loads plugin blocker before pytest starts.
"""
import sys
import os

# Set environment variable early
os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")

# Add paths for imports
code_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(code_dir)

if code_dir not in sys.path:
    sys.path.insert(0, code_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import and apply plugin blocker BEFORE importing pytest
try:
    from code import pytest_plugin_blocker
except ImportError:
    try:
        import pytest_plugin_blocker
    except ImportError:
        pass

# Now import and run pytest
import pytest

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-vv", "tests"]
    sys.exit(pytest.main(args))
