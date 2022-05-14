<?php

# Functions

function msg(string $msg): void
{
    echo PHP_EOL . $msg;
}

# STARTS THE PROCESSING

# Config

$host = '0.0.0.0';
$base = 'games';
$login = 'game';
$password = 'azerty';

msg("Starting the migration");

$connection = new \PDO("mysql:host=$host;dbname=$base", $login, $password, [\PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8']);
$connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

# Remove all the foreigns keys
$keys = [
    'games' => 'games_ibfk_1',
    'games_meta' => 'games_meta_ibfk_1',
    'history' => 'history_ibfk_1',
    'trades' => 'trades_ibfk_1',
];

foreach ($keys as $table => $constraint) {
    $connection->exec("ALTER TABLE $table DROP FOREIGN KEY $constraint;");
}

# Rename the game_id field to version_id
$tables = ['games_meta', 'history', 'trades'];

foreach ($tables as $table) {
    $connection->exec("ALTER TABLE $table CHANGE game_id version_id SMALLINT(11) UNSIGNED;");
}

# Create the versions table
$query = $connection->prepare('CREATE TABLE IF NOT EXISTS versions(version_id SMALLINT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, platform INT NOT NULL, game INT NOT NULL) ENGINE=INNODB;');
$query->execute();

$query = $connection->prepare('CREATE UNIQUE INDEX games_platforms ON versions(platform, game);');
$query->execute();

# Loop on every game
$gamesIndex = [];

$query = $connection->prepare('SELECT * FROM games');
$query->execute();

while ($game = $query->fetch()) {
    msg("Processing game with ID #{$game['id']}");

    # Creation of the version and cleaning duplicates
    if (array_key_exists($game['title'], $gamesIndex)) {
        $insertQuery = $connection->prepare("INSERT INTO versions (platform, game) VALUES ({$game['platform']}, {$gamesIndex[$game['title']]})");
        $insertQuery->execute();
        $lastId = $connection->lastInsertId();
        $insertQuery->closeCursor();
        
        msg("Deleting {$game['title']}");
        $insertQuery = $connection->prepare("DELETE FROM games WHERE id = {$game['id']}");
        $insertQuery->execute();
        $insertQuery->closeCursor();

    } else {
        $insertQuery = $connection->prepare("INSERT INTO versions (platform, game) VALUES ({$game['platform']}, {$game['id']})");
        $insertQuery->execute();
        $lastId = $connection->lastInsertId();
        $insertQuery->closeCursor();

        $gamesIndex[$game['title']] = $game['id'];
    }

    # Updating meta
    $updateQuery = $connection->prepare("UPDATE games_meta SET version_id = $lastId WHERE version_id = {$game['id']}");
    $updateQuery->execute();

    # Updating history
    $updateQuery = $connection->prepare("UPDATE history SET version_id = $lastId WHERE version_id = {$game['id']}");
    $updateQuery->execute();

    # Updating trades
    $updateQuery = $connection->prepare("UPDATE trades SET version_id = $lastId WHERE version_id = {$game['id']}");
    $updateQuery->execute();

    $updateQuery->closeCursor();
}

# Remove the platform field in the games table
$query = $connection->prepare('ALTER TABLE games DROP COLUMN platform;');
$query->execute();

# Setting FK
