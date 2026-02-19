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
	python run_pytest.py

