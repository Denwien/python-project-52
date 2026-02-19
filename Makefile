PYTHON := python

install:
	uv sync --frozen --all-groups

build:
	./build.sh

migrate:
	$(PYTHON) manage.py migrate --noinput

collectstatic:
	$(PYTHON) manage.py collectstatic --noinput

test:
	cd code && PYTHONPATH=..:$$PYTHONPATH PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run python -c "import sys; sys.path.insert(0, '..'); from code import pytest_plugin_blocker; import pytest; pytest.main(['-vv', 'tests'])"

