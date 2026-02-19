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
	PYTHONPATH=. PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -c "import pytest_plugin_blocker; import pytest; pytest.main(['-vv', 'tests', '-p', 'no:pytest_dotenv', '-p', 'no:pytest-dotenv'])"

