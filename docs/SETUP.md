# Starting a project

## Locally (DEV)

In the root folder, copy the file _configuration.json.dist_ to _configuration.json_ and fill it with your values. The MySQL credentials are visible in the _docker-compose.yml_ in the root folder.

Next, just do a __make start__, and then run __make test__ to run the tests and import the local DB with test features. You're good to go!

## Production

_Reminder_: the empty database contains a default user.
Credentials are:
* username: _foo_
* password: _bar_

Change them as soon as your project is running!

The usual process to setup a project is the following:
* Import the empty database (available at the root of the folder).
* Run all the migrations ([see here](./MIGRATIONS.md))
* Deploy the code.
* Configure the application.
* Start the application.
* Change your default credentials.

## 1- Importing the dabase

Nothing much to say here, import the empty database in to your MySQL server.

## 2- Deploying the code.

Same here: just upload the code on your server.

## 3- Configuring the application

In the root folder, copy the file _configuration.json.dist_ to _configuration.json_ and fill it with your values.

## 4- Starting the application

Make your gunicorn server to launch the application __app.py__.

## 5- Change your default credentials
As explained above, change your password and you username and email. Then,
using the POST _/user/1_ endpoint, change your credentials, and the _user/renew-token_ to change your token. More information is available in the API documentation.