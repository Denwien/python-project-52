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
	cd code && PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run python -m pytest_entrypoint -vv tests

