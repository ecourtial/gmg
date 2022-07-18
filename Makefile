.PHONY: test

test:
	make import_db && docker compose exec python bash -c 'make test_command_python'

linter:
	docker compose exec python pylint --rcfile=standard.rc src/ ./app.py

start:
	docker compose up

python:
	docker compose exec python bash

mysql:
	docker compose exec mysql bash -c 'mysql -u game -pazerty games'

import_db:
	docker compose exec mysql bash -c 'cd /code && make import_db_command'

export_db:
	docker compose exec mysql bash -c 'cd /code && mysqldump -u game -pazerty games > test/games_test.sql'

# updates the requirements from PIPENV (need to rebuild the pyton container after that)
requirements:
	docker compose exec python bash -c "cd docker/python && pipenv lock -r > ./requirements.txt"

## Containers internal command
import_db_command:
	mysql -u game -pazerty games < test/games_test.sql

test_command_python:
	python -m unittest discover .
