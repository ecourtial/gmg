.PHONY: test

test:	
	docker-compose exec python bash -c "python -m unittest discover ."

linter:
	docker-compose exec python pylint --rcfile=standard.rc src/ ./app.py

start:
	docker-compose up

python:
	docker-compose exec python bash
