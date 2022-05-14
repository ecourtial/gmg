.PHONY: test

test:
	docker-compose exec mysql bash -c "mysql -u game -pazerty games < var/test_games.sql" \
	&& docker-compose exec python bash -c "python -m unittest discover ."

linter:
	docker-compose exec python pylint --rcfile=standard.rc src/ ./app.py

start:
	docker-compose up

python:
	docker-compose exec python bash

# updates the requirements from PIPENV (need to rebuild the pyton container after that)
requirements:
	docker-compose exec python bash -c "cd docker/python && pipenv lock -r > ./requirements.txt"

## Containers internal command
test_command_sql:
	mysql -u game -pazerty games < var/test_games.sq

test_command_python:
	python -m unittest discover .