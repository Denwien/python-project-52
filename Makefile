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
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest -vv tests -p no:pytest_dotenv -p no:pytest-dotenv -p no:pytest_env -p no:pytest-env

