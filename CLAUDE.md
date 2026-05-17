# Project Context

This project is an API only application to manage a video games collection. It handles many elements, such as games, version, attributes of the games, the copy, transaction (selling or buying games), notes.

It provides a basic REST+JSON api.

## Architecture

The main controller of the project is the _app.py_ file at the root of the project. Is also where everything is loaded (configuration, create of the SQL connection...).

Then everything else (of the code) is stored in the _src_ folder.

* _connection_ contains the class to manage the connection to the database;
* _controller_ contains each of the controllers specific to a resource type. Note that they have a base class that contains common method, for instance for CRUD operations;
* _entity_ contrains classes that represent ressources;
* _exception_ contains all the various exception classes;
* _helper_ contains various helpers;
* _repository_ contains repositories classes that allow to load and persist ressources. Note that they have two levels of base classes that contains shared logic to interact with the DB for the first one, and performs common operations (like loading, filtering...) for the second one;
* _service_ contains services classes, where "business logic" might be stored to keep controllers lightweight.

## Entities

The entities represent the ressources managed by the API. One file = one class = one ressource.

Inside each entity class, we will find a constructor, getters and setters, and a method to serialize the object before returning it to the client.

But the most important part is probably all the metadata at the beginning of the class. Let's take this example:

```
    expected_fields: dict[str, Any] = {
        'title': {'field': 'title', 'method': '_title', 'required': True, 'type': 'text'},
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
        'id': {'field': 'id', 'origin': 'native', 'type': 'int'},
        'versionCount': {'field': 'versionCount', 'origin': 'computed', 'type': 'int'}
    }

    table_name = 'games'
    primary_key = 'id'
```

* _expected_fields_ is an array that lists all the fields in the MySQL table. The key of the array is the key in the payload. For each field, we have a _field_ value that contains the name of the MySQL field. _method_ is the suffix of the getters and setters. For each field, you also have a _type_ metadata, which represents the data type, and also an optionnal _default_ key for optional values.
* _authorized_extra_fields_for_filtering_ is an array of the key in the URL that represent fields we can filter on. We have the type, but also the 'origin', which is 'native' or 'computed', the first case being when it is a direct filter on the value in the database.
* _table_name_ is the name of the MySQL table.
* _primary_key_ is the name of the primary key.

Sometimes, things are more rigorous.
We have this case with the _copy_ entity. For some fields we can find things like this:

```
'type': 'strict-text',
        'allowed_values': {
```
We notice that the type is "strict-text", hence we have a sub-array that contains all the allowed values for this field. We cannot list them all here, because they are specific to a field inside an entity.

The allowd types are:
* _strict-text_: is a list of supported choices;
* _text_: a text of undefined sized;
* _int_: well, it is an integer;
* _string_: short text (varchar 255).

The logical relation between the entities can be found in the _RESOURCES.md_ file in the _docs_ folder at the root of the project.

## Running or testing the app locally

* Running the app is not required for the AI agent.
* But testing it is usefull to detect added defects. Running the _make test_ command run the API test suite.
* Tests are located in the _tests_ folder.
* The stack uses _unittest_.
