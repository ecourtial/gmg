.PHONY: test

# I added the version of Python in the commande becaus I run multiple versions on my machine
test:	
	python3 -m unittest discover .

linter:
	docker-compose exec python pylint --rcfile=standard.rc src/