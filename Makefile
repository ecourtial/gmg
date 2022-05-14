.PHONY: test

test:
	docker-compose exec mysql bash -c 'cd /code && make test_command_sql' \
	&& docker-compose exec python bash -c 'make test_command_python'

linter:
	docker-compose exec python pylint --rcfile=standard.rc src/ ./app.py

start:
	docker-compose up

python:
	docker-compose exec python bash

mysql:
	docker-compose exec mysql bash

# updates the requirements from PIPENV (need to rebuild the pyton container after that)
requirements:
	docker-compose exec python bash -c "cd docker/python && pipenv lock -r > ./requirements.txt"

## Containers internal command
test_command_sql:
	mysql -u game -pazerty games < test/games_test.sql

test_command_python:
	python -m unittest discover .