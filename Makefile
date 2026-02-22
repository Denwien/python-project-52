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
	uv run pytest --ds=task_manager.settings --reuse-db

