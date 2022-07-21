# Migrations and update guide

If you already have the application running and want to update it to the last version, you need to proceed as explained below.

* 1) Stop your server.
* 2) Get and update the source code form the last version (tip: download everything from Github and replace it in your folder).
* 3) Run all the migrations you need using the following command:
```make migration FILE={migration_file}```
for instance
```make migration FILE=4.1.0```.
* 4) Restart your server.
