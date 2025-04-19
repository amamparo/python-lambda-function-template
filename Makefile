install:
	poetry install --no-root

run:
	poetry run python -m src.main

lint:
	poetry run pylint src tests aws

types:
	poetry run mypy src tests aws

test:
	poetry run python -m unittest discover -s 'tests' -p '*.py'

diff:
	cdk diff --fail

deploy:
	cdk deploy