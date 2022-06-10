# API

## Introduction

There are 7 kinds of resource in this application:
- users;
- platforms;
- games;
- versions;
- copies;
- stories;
- transactions.

Each endpoint is accessible using the prefix _api/v1/_.

## 1- Users

The _user_ resource is very specific, for security concerns. The following endpoints are available:

| Endpoint                        | Role                                                                                                                          |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| user/authenticate (POST)        | Authenticate the user using [basic HTTP authentication](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Authorization).|
| user (GET)                      | Get a a given user according to one of the following filter: id, email or userName. For instance: user?id=1                   |
| user (POST)                     | Creates a user.                                                                                                               |
| user/{id} (PATCH)               | Updates some values of the user.                                                                                              |
| user/renew-token (POST)         | Renews the current user token and return it.                                                                                  |
|

By default, a user created with the API is disabled. You have to user the PATCH method to change the 'active' field to true.

The editable fields are the following:
* email
* password
* active
* username

## 2- Other resources:

### 1- CRUD operations

The other resources follow the same pattern for CRUD operations.
There are 4 methods available:
* GET (e.g: _game/1_)
* POST (e.g: _game_)
* PATCH (e.g: _game/1_)
* DELETE (e.g: _game/1_)

### 2- Basic filtering

There is also another one to search for resources. The endpoint uses the GET verb and all the parameters are in the query string. Note that this time the resource in the URI is plural. Let's see an example:

```versions?toDo[]=1&hallOfFameYear[]=2008&hallOfFameYear[]=2012&orderBy[]=Id-desc&page=2&limit=5```

In the above example you want to search for:
* resource of type version;
* that are in your todo list (note the toDo = 1 for a boolean to _true_);
* which have the _hallOfFameYear_ field set to 2008 or 2012;
* ordered by the version id, DESC;
* the second page of the result;
* each page containing a maximum of 5 results.

_Tip_: you can also order by random. Just use one filter value for _orderBy_ with _rand as the filter's value:
```versions?toDo[]=1&hallOfFameYear[]=2008&hallOfFameYear[]=2012&orderBy[]=rand&page=2&limit=5```

### 3- Filtering on numeric fields

A numeric field can also be used for sorting. Let's look at the following example:

```versions?copyCount[]=gt-0```

Here you want to get all the versions (with the defaut pagination: first page, max result limit set to 30) but only the ones who have copies (hence the > 0 operator).


| API syntax | Signification |           Example              |
|------------|---------------|--------------------------------|
|lt          |Lesser than    |```versions?copyCount[]=lt-2``` |
|gt          |Greater than   |```versions?copyCount[]=gt-1``` |
|eq          |Equal          |```versions?copyCount[]=eq-1``` |
|neq         |Not equal      |```versions?copyCount[]=neq-1```|
