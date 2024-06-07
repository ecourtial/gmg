# GMG (Give Me a Game)
[![CircleCI](https://circleci.com/gh/ecourtial/gmg/tree/master.svg?style=svg)](https://circleci.com/gh/ecourtial/gmg/tree/master) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gmg&metric=alert_status)](https://sonarcloud.io/dashboard?id=gmg) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/ecourtial/gmg/graphs/commit-activity) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/ecourtial/gmg) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/ecourtial/gmg/blob/master/LICENSE)

## Description :notebook:

### A back-end application for your video games inventory

GMG is an educational test project. Being a PHP programmer, I developed this project using Python 3.x and Flask 2.
The goal of this application is to expose API endpoints to manage you video games collection, with various features.
There is no graphical interfaces, only API endpoints. Data is stored in MySQL.

### What? No user interface?

I did not include a GUI because:
- I am not good at it;
- it would have implied extra work;
- coupling between the front and the back;
- taste and colors...

The developer who want to use this application is free to develop it's own front app connected through the REST endpoints, it is a classic. You can create a classy shiny state of the art front app or just a basic one using only one part of the features the back-end offers.

However, I developed my own front app, available [here](https://github.com/ecourtial/gmg-front), using PHP 8.1 and Symfony. You can use it if you don't have specific needs. Note: it does not include the support for all the features given by the back application.

## Utilization

A basic documentation is available:
* [How to install the project](docs/SETUP.md)
* [Introduction to the API](docs/API.md)
* [Resources managed by the application and their API representation](docs/RESOURCES.md)
* [Migrations and update guide](docs/MIGRATIONS.md)

## Stack :light_rail:

* Docker
* Nginx
* Gunicorn
* Python 3.10
* Flask 2
* Circle CI
* unittest
* pylint
* MySQL 8

## Changelog

The changelog is available [here](CHANGELOG.md)
