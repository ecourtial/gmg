# GMG (Give Me a Game)
[![CircleCI](https://circleci.com/gh/ecourtial/gmg/tree/master.svg?style=svg)](https://circleci.com/gh/ecourtial/gmg/tree/master) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gmg&metric=alert_status)](https://sonarcloud.io/dashboard?id=gmg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/ecourtial/gmg/graphs/commit-activity) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/ecourtial/gmg) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/ecourtial/gmg/blob/master/LICENSE)

## Description :notebook:

A personal educational test project to manage my video games collection. Games can be sorted by support,
todo list, watch list, ranking...

## Utilization

* In dev mode: just do a __docker compose up__. In production, make your gunicorn server to launch the application __app.py__.

* An empty database is given in the repository: just import it.

* In the root folder, copy the file _configuration.json.dist_ to _configuration.json_ and fill it with your values.

* Once the application is running, go to __/register__ to create an account.

* Then go to your database to enable the user you just created. That's it.

## Stack :light_rail:

* Docker
* Nginx
* Gunicorn
* Python 3.7
* Flask
* Jinja 2
* Circle CI
* jQuery
* RequireJS
* unittest
* pylint
* Ansible

## Changelog

### 3.1.0
* Added a "todo with help" icon in the game list if the game is to be completed with some help.
* The game id is now visible in the game lists.
* Added a History menu to log the games we finish (watch or play).

### 3.0.1
* Fixed a bug when adding a new game while edition was still working.

## Todo
Yet the project is fully working, there are some features or elements to improve:
* Internationalization.

* Add a logical check if the user already exists when creating an account.

* Improve error handling on front-end... after improving it on back-end (return the proper HTTP headers according to the error).

* Add the possibility to remove a platform.

* Improve form validation.

* Add the possibility to store the user id of the user who registered a game and the id of the last user to edit a given game.

* Add unit tests (so far only the game entity is covered).
