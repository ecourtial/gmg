# Starting a project

_Reminder_: the empty database contains a default user.
Credentials are _foo_:_bar_. Change them when you start your project.

The usual process to setup a project is the following:
* Import the database.
* Deploy the code.
* Configure the application.
* Start the application.
* Change your default credentials.

## 1- Importing the dabase

Nothing much to say here, import the empty database in to your MySQL server.

## 2- Deploying the code.

* In dev mode: you have nothing to do.
* In production mode: just upload the code on your server.

## 3- Configuring the application

In the root folder, copy the file _configuration.json.dist_ to _configuration.json_ and fill it with your values.

## 4- Starting the application

* In dev mode: just do a __make start__, and then run __make test__ to import the local DB with features. 
* In production, make your gunicorn server to launch the application __app.py__.

## 5- Change your default credentials (for production only)

Using the POST _/user/1_ endpoint, change your credentials, and the _user/renew-token_ to change your token. More information are available in the API documentation.