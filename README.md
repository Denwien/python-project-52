# python-project-52

[![hexlet-check](https://github.com/Denwien/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Denwien/python-project-52/actions/workflows/hexlet-check.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-52&metric=alert_status&branch=main)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Denwien_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Denwien_python-project-52)

## Description

Task Manager is a web application built with Django.

It allows users to create tasks, assign statuses, labels and executors,
as well as filter tasks by different criteria.

The project includes:

- user authentication
- task management (CRUD)
- task filtering
- automated tests
- static code analysis with SonarCloud

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager)
- PostgreSQL (production) or SQLite (default, development)

## Installation

    git clone https://github.com/Denwien/python-project-52.git
    cd python-project-52

Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
if you don't have it:

    curl -LsSf https://astral.sh/uv/install.sh | sh

Install dependencies, collect static files and apply migrations:

    make build

Or step by step:

    make install       # install dependencies via uv
    make collectstatic # collect static files
    make migrate       # apply database migrations

## Configuration

Copy `.env.example` to `.env` and set the required variables:

| Variable               | Description                        | Default          |
|------------------------|------------------------------------|------------------|
| `SECRET_KEY`           | Django secret key                  | `dev-secret-key` |
| `DEBUG`                | Enable debug mode (True/False)     | `False`          |
| `ALLOWED_HOSTS`        | Comma-separated list of hosts      | `localhost`      |
| `DATABASE_URL`         | Database URL (e.g. postgres://...) | SQLite           |
| `ROLLBAR_ACCESS_TOKEN` | Rollbar error tracking token       | —                |

## Running

    uv run python manage.py runserver

## Testing

    make test

With coverage report:

    make test-coverage

## Linting

    uv run ruff check .
