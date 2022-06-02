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

| Endpoint                        | Role                                                     |
|---------------------------------|----------------------------------------------------------|
| user/authenticate               | Authenticate the user using [basic HTTP authentication](https://developer.mozilla.org/fr/docs/Web/HTTP/Headers/Authorization).   |
| user (GET)                      | Get a a given user according to one of the following filter: id, email or userName. For instance: user?id=1                    |
| user (POST)                  | Creates a user.                                |
| user/{id} (PATCH)                      | Updates some values of the user. |
| user/renew-token (POST)  | Renews the current user token and return it.                       |
|

By default, a user created with the API is disabled. You have to user the PATCH method to change the 'active' field to true.

The editable fields are the following:
* email
* password
* active
* username

## 2- Other resources

The other resources follow the same pattern for CRUD operations.
There are 4 methods available:
* GET (e.g: _game/1_)
* POST (e.g: _game_)
* PATCH (e.g: _game/1_)
* DELETE (e.g: _game/1_)

There is also another one to search for resources. The endpoint uses the GET verb and all the parameters are in the query string. Note that this time the resource in the URI is plural. Let's see an example:

_versions?hallOfFameYear[]=2008&hallOfFameYear[]=2012&order_by=Id_order=desc&page=2&limit=5_

In the above example you want to search for:
* resource of type version;
* which have the _hallOfFameYear_ field set to 2008 or 2012;
* ordered by the version id, DESC;
* the second page of the result;
* each page containing a maximum of 5 results.
