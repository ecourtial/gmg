# Resources

The application relies on 6 resources (not including the users).

| Resource                        | Role                                                                                                                           |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Platform                        | The support of a game. For instance: _Playstation II_.                                                                         |
| Game                            | A given game. For instance: _Fifa 2000_                                                                                        |
| Version                         | A version of a given game. For instance: _Fifa 2000_ on PC.                                                                    |
| Copy                            | A physical or virtual copy. For instance: the big box version of _Fifa 2000_ on PC.                                            |
| Story                           | An instance of what you did with a game. For instance: you watched a playthrough of the _Fifa 2000_ PC version in april 2020.  |
| Transaction                     | A record of buying, solding, lending a copy of a game.                                                                        |

## Relations

![Relations](resources.svg "Relations")

# Resources in details

## User

| Field    | Type    | Editable | Unique | Role                  | Notes                                              |
|----------|---------|----------|--------|-----------------------|----------------------------------------------------|
| id       | int     | No       |  Yes   | The user unique id.   |                                                    |
| email    | string  | Yes      |  Yes   | The user email.       |                                                    |
| username | string  | Yes      |  Yes   | The user pseudo.      |                                                    |
| password | string  | Yes      |  No    | The user password.    |                                                    |
| active   | bool    | Yes      |  No    | Is the user active?   |                                                    |
| token    | string  | No       |  No    | The user API token.   | Only visible throught the _authenticate_ endpoint. |

## Platform

| Field        | Type    | Editable | Unique | Role                                           | Notes                                              |
|--------------|---------|----------|--------|------------------------------------------------|----------------------------------------------------|
| id           | int     | No       |  Yes   | The platform unique id.                        |                                                    |
| name         | string  | Yes      |  Yes   | The platform name.                             |                                                    |
| versionCount | int     | No       |  No    | How many games are registered on this platform.|                                                    |

## Game

| Field        | Type    | Editable | Unique | Role                                           | Notes                                              |
|--------------|---------|----------|--------|------------------------------------------------|----------------------------------------------------|
| id           | int     | No       |  Yes   | The game unique id.                            |                                                    |
| title        | string  | Yes      |  Yes   | The game title.                                |                                                    |
| notes        | string  | Yes      |  No    | Your notes.                                    |                                                    |
| versionCount | int     | No       |  No    | How many versions are registered for this game.|                                                    |

## Version

| Field                    | Type  | Editable | Unique | Role                                                                        |      Notes                              |
|--------------------------|-------|----------|--------|-----------------------------------------------------------------------------|-----------------------------------------|
| id                       | int   | No       |  Yes   | The version unique id.                                                      |                                         |
| platformId               | int   | Yes      |  Yes   | The game id of the version.                                                 |                                         |
| releaseYear              | int   | Yes      |  No    | The release year of the version                                             |                                         |
| todoSoloSometimes        | bool  | Yes      |  No    | You wan to play this version of the game in solo from time to time.         |                                         |
| todoMultiplayerSometimes | bool  | Yes      |  No    | You wan to play this version of the game in multiplayer from time to time.  |                                         |
| singleplayerRecurring    | bool  | Yes      |  No    | You wan to play this version of the game in solo regularly.                 |                                         |
| multiplayerRecurring     | bool  | Yes      |  No    | You wan to play this version of the game in multiplayer regularly.          |                                         |
| toDo                     | bool  | Yes      |  No    | This version of the game is in your todo list.                              |                                         |
| toBuy                    | bool  | Yes      |  No    | You want to buy this version of the game.                                   |                                         |
| toWatchBackground        | bool  | Yes      |  No    | You want watch a walkthrough of this version of the game, in background.    |                                         |
| toWatchSerious           | bool  | Yes      |  No    | You want watch a walkthrough of this version of the game, with attention.   |                                         |
| toRewatch                | bool  | Yes      |  No    | You want watch a walkthrough of this version of the game, from time to time.|                                         |
| topGame                  | bool  | Yes      |  No    | This version is a top game for you.                                         |                                         |
| hallOfFame               | bool  | Yes      |  No    | This version of the game is in your Hall of Fame.                           |                                         |
| hallOfFameYear           | int   | Yes      |  No    | Year of presence in your hall of fame.                                      |                                         |
| hallOfFamePosition       | int   | Yes      |  No    | Position, within the given year, in your hall of fame.                      |                                         |
| playedItOften            | bool  | Yes      |  No    | You played this version of the game, a lot.                                 |                                         |
| ongoing                  | bool  | Yes      |  No    | You are currently playing at this version of the game.                      |                                         |
| comments                 | string| Yes      |  No    | Commments.                                                                  |                                         |
| todoWithHelp             | bool  | Yes      |  No    | To do with help, cheats, tips, walkthrough...                               |                                         |
| bestGameForever          | bool  | Yes      |  No    | This version is one of you best game forever, no matter how old it is.      |                                         |
| toWatchPosition          | int   | Yes      |  No    | The position in your to watch list.                                         |                                         |
| toDoPosition             | int   | Yes      |  No    | The position in your to todo list.                                          |                                         |
| finished                 | bool  | Yes      |  No    | Did you ever finish this version of the game?                               |                                         |
| platformName             | string| No       |  Yes   | The name of the platform.                                                   |                                         |
| gameTitle                | string| No       |  Yes   | The title of the game related to this version.                              |                                         |
| storyCount               | int   | No       |  No    | How many stories do you have for this version.                              |                                         |
| copyCount                | int   | No       |  No    | How many copes do you have for this version.                                |                                         |

## Story

| Field                    | Type  | Editable | Unique | Role                                                                        |         Notes                           |
|--------------------------|-------|----------|--------|-----------------------------------------------------------------------------|-----------------------------------------|
| id                       | int   | No       |  Yes   | The version unique id.                                                      |                                         |
| versionId                | int   | Yes      |  No    | The id of the version the story relates to.                                 |                                         |
| releaseYear              | int   | Yes      |  No    | The year when this story happened.                                          |                                         |
| position                 | int   | Yes      |  No    | Position, within the given year, of this story.                             |                                         |
| watched                  | bool  | Yes      |  No    | Did you watch a video of the game?                                          |                                         |
| played                   | bool  | Yes      |  No    | Did you played at the game?                                                 |                                         |
| platformName             | string| No       |  No    | The name of the platform.                                                   |                                         |
| gameTitle                | string| No       |  No    | The title of the game related to this story.                                |                                         |

## Copy

| Field                    | Type  | Editable | Unique | Role                                                                        |         Notes                           |
|--------------------------|-------|----------|--------|-----------------------------------------------------------------------------|-----------------------------------------|
| id                       | int   | No       |  Yes   | The version unique id.                                                             |                                  |
| versionId                | int   | Yes      |  No    | The id of the version the story relates to.                                        |                                  |
| original                 | bool  | Yes      |  No    | Is the copy an original (not a copy from an original)?                             |                                  |
| language                 | string| Yes      |  No    | Any language value. We recommend to use ISO standards, or _multi_ if mutilanguage. |                                  |
| boxType                  | string| Yes      |  No    | Type of the box (See allowed types below).                                         |                                  |
isBoxRepro                 | bool   | Yes     |  No    | Is the box a reproduction?|
| casingType               | string| Yes      |  No    | Casing type of the box (See allowed types below).                                  |                                  |
| supportType              | string| Yes      |  No    | The game support type (See allowed types below).                                   |                                  |
| onCompilation            | bool  | Yes      |  No    | Is the copy of the game on a compilation?                                          |
| region            | string  | Yes      |  No    | Region lock of the game? (See allowed types below).                                        |                                  |
| reedition                | bool  | Yes      |  No    | Is the copy of the game on a reedition, like a platinum, a classic one?            |                                  |
| hasManual                | bool  | Yes      |  No    | Does the copy has a manual?                                                        |                                  |
| status                   | string| Yes      |  No    | Do you currently have this copy (See allowed types below)?                         |                                  |
| type                     | string| Yes      |  No    | Type of the copy (See allowed types below)?                                        |                                  |
| is_rom                   | bool  | Yes      |  No    | Is the copy a ROM?                                                                 |                                  |
| comments                 | string| Yes      |  No    | Commments.                                                                         |                                  |
| platformName             | string| No       |  No    | The name of the platform.                                                          |                                  |
| gameTitle                | string| No       |  No    | The title of the game related to this copy.                                        |                                  |

### Allowed types for _boxType_

| Value        | Meaning                                                 |
|--------------|---------------------------------------------------------|
|Big box       | The big cardboard boxes we had for PC games in the 90's.|
|Medium box    | The medium cardboard boxes we find sometimes.           |
|Special box   | The special cardboard boxes we find sometimes.          |
|Cartridge box | Cardboard boxes for Nintendo 64 for instance.           |
|Other         | Other cases with special boxes                          |
|None          | No box at all.                                          |

### Allowed types for _casingType_

| Value                | Meaning                                                                 |
|----------------------|-------------------------------------------------------------------------|
|DVD-like              | The DVD-like casing (Genesis/Megadrive, Saturn, PS2, Gamecube, Xbox...).|
|CD-like               | CD-like Casing (Playstation, Dreamcast, PC...).                         |
|Cardboard sleeve      | Just a sleeve for the disc.                                             |
|Paper sleeve          | Just a sleeve for the disc.                                             |
|Plastic sleeve        | Just a sleeve for the disc.                                             |
|Other                 | Other casing.                                                           |
|None                  | For instance, a loose CD.                                               |

### Allowed types for _supportType_

| Value                | Meaning                                        |
|----------------------|------------------------------------------------|
|Blu-ray               |                                                |
|DVD-ROM               |                                                |
|CD-ROM                |                                                |
|GD-ROM                |                                                |
|MINI-Blu-ray          |                                                |
|MINI-DVD-ROM          |                                                |
|MINI-CD-ROM           |                                                |
|Cartridge             |                                                |
|3.5-inch floppy       |                                                |
|5.25-inch floppy      |                                                |
|Other disc            |                                                |
|Other floppy          |                                                |
|External drive        |                                                |
|None                  |                                                |

### Allowed types for _status_

| Value                | Meaning                                        |
|----------------------|------------------------------------------------|
|In                    | The copy enter your stock.                     |
|Out                   | The copy leaves your stock.                    |

### Allowed types for _type_

| Value                | Meaning                                        |
|----------------------|------------------------------------------------|
|Physical              | The copy is physical.                          |
|Virtual               | The copy is virtual (ex: bought on _Steam_).   |


### Allowed types for _region_

| Value                | Meaning                                        |
|----------------------|------------------------------------------------|
|PAL                   | Europe, New Zealand, Australia, Middle East, India, South Africa                                          |
|JAP                   | Japan and Asia (NTSC-J)                        |
|NTSC                  | North America and South America (NTSC-U)       |
|CHINA                 | China (NTSC-C)                                 |


## Transaction

| Field                    | Type  | Editable | Unique | Role                                                                        |         Notes                           |
|--------------------------|-------|----------|--------|-----------------------------------------------------------------------------|-----------------------------------------|
| id                       | int   | No       |  Yes   | The version unique id.                                                      |                                         |
| versionId                | int   | Yes      |  No    | The version id of the game the transaction relates to.                      |                                         |
| copyId                   | int   | Yes      |  No    | The id of the copy the transaction relates to (might be null if the copy has been sold, see below).                              |                                         |
| year                     | int   | Yes      |  No    | The year when this transaction happened.                                    |                                         |
| month                    | int   | Yes      |  No    | The month when this transaction happened.                                   |                                         |
| day                      | int   | Yes      |  No    | The day when this transaction happened.                                     |                                         |
| type                     | string| Yes      |  No    | Type of the transaction (See allowed types below)?                          |                                         |
| notes                    | string| Yes      |  No    | Commments.                                                                  |                                         |
| platformName             | string| No       |  No    | The name of the platform.                                                   |                                         |
| gameTitle                | string| No       |  No    | The title of the game related to this transaction.                          |                                         |

### Allowed types for _type_

| Value                | Meaning                                        |
|----------------------|------------------------------------------------|
|Bought                | You bought the copy.                           |
|Sold                  | You sold the copy.                             |
|Loan-out              | You loan the copy to someone.                  |
|Loan-out-return       | Someone returns you the copy after a loan.     |
|Loan-in               | Someone loans you the copy.                    |
|Loan-in-return        | After a loan, you return the copy.             |

_NOTE_: when creating a transaction, the status of the copy will be altered accordingly to the type of the transaction. The drawback of this aspect is that if you edit a transaction by changing its _copy_id_, the previously targeted copy will be in a bad status, so act accordingly to update it too and set it to the good status.

On top of that, if the transaction is of type "Sold", the copy will be deleted.

Finally, you cannot edit a transaction if the copy no longer exists. If you did something wrong, delete the transaction and start over.

## Notes

| Field        | Type    | Editable | Unique | Role                                           | Notes                                              |
|--------------|---------|----------|--------|------------------------------------------------|----------------------------------------------------|
| id           | int     | No       |  Yes   | The note unique id.                        |                                                    |
| title         | string  | Yes      |  No   | The note title.                             |                                                    |
| content | string     | Yes       |  No    | The text of the note.|  