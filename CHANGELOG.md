# Changelog

## 4.4.0
* Added a new feature: notes.

## 4.3.0
* Added a new _isBoxRepro_ field to the copy entity.
* Added a new box type: _Medium box_.
* Added a new box type: _Special box_.

## 4.2.0
* Added new support types: Blu-ray, MINI-Blu-ray, External drive.
* Added region type for a copy: PAL, JAP... The migration is included, setting the default value to PAL.

## 4.1.1
* Security updates.

## 4.1.0

### New features
* The copy entity has a new _is_rom_ field to define if the copy is a ROM or not (for emulation for instance).
A migration file is available in the _migrations_ folder (see [Migrations and update guide](docs/MIGRATIONS.md)).
* The copy _casingType_ field accepts a new value: _Plastic tube_.
