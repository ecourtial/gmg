# Migrations and update guide

* 1) Stop serving the application (just keep MySQL running).
* 2) Get and update the source code form the last version (tip: download everything from Github and replace it in your folder).
* 3) Run all the migrations you need using the following command:
```make migration FILE={migration_file}```
for instance
```make migration FILE=4.1.0```.
* 4) Restart your server.
