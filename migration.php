<?php

# Functions

function msg(string $msg): void
{
    echo PHP_EOL . $msg;
}

function insertVersion(int $gameId, int $platform, array $meta): int
{
    global $connection;

    $hofPosition = (int)$meta['hall_of_fame_position'];
    $isHof = (int)$meta['hall_of_fame'];
    $hofYear = (int)$meta['hall_of_fame_year'];

    $insertQuery = $connection->prepare(
        "INSERT INTO versions (platform_id, game_id, todo_solo_sometimes, todo_multiplayer_sometimes, singleplayer_recurring, multiplayer_recurring, to_do, to_buy, to_watch_background, to_watch_serious, to_rewatch, top_game, hall_of_fame, hall_of_fame_year, hall_of_fame_position, played_it_often, ongoing, comments, todo_with_help, bgf, to_watch_position, to_do_position) "
        .  "VALUES ({$platform}, {$gameId}, {$meta['todo_solo_sometimes']}, {$meta['todo_multiplayer_sometimes']}, {$meta['singleplayer_recurring']}, {$meta['multiplayer_recurring']}, {$meta['to_do']}, {$meta['to_buy']}, {$meta['to_watch_background']}, {$meta['to_watch_serious']}, {$meta['to_rewatch']}, {$meta['top_game']}, $isHof, $hofYear, $hofPosition, {$meta['played_it_often']}, {$meta['ongoing']}, NULL, {$meta['todo_with_help']}, {$meta['bgf']}, {$meta['to_watch_position']}, {$meta['to_do_position']})"
    );
    $insertQuery->execute();
    $lastId = $connection->lastInsertId();
    $insertQuery->closeCursor();

    return $lastId;
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
$tables = ['history'];

foreach ($tables as $table) {
    $connection->exec("ALTER TABLE $table CHANGE game_id version_id SMALLINT(11) UNSIGNED;");
}

# Rename the table history to stories
$connection->exec("RENAME TABLE history to stories");

# Create the versions table
$createStatement = "
CREATE TABLE IF NOT EXISTS versions(
  `version_id` SMALLINT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
  `platform_id` TINYINT UNSIGNED NOT NULL, 
  `game_id` SMALLINT UNSIGNED NOT NULL,
  `release_year` SMALLINT NOT NULL DEFAULT '0', 
  `todo_solo_sometimes` tinyint unsigned NOT NULL DEFAULT '0', 
  `todo_multiplayer_sometimes` tinyint unsigned NOT NULL DEFAULT '0', 
  `singleplayer_recurring` tinyint unsigned NOT NULL DEFAULT '0', 
  `multiplayer_recurring` tinyint unsigned NOT NULL DEFAULT '0', 
  `to_do` tinyint unsigned NOT NULL DEFAULT '0', 
  `to_buy` tinyint unsigned NOT NULL DEFAULT '0', 
  `to_watch_background` tinyint unsigned NOT NULL DEFAULT '0', 
  `to_watch_serious` tinyint unsigned NOT NULL DEFAULT '0', 
  `to_rewatch` tinyint unsigned NOT NULL DEFAULT '0', 
  `top_game` tinyint unsigned NOT NULL, 
  `hall_of_fame` tinyint unsigned NOT NULL DEFAULT '0', 
  `hall_of_fame_year` smallint unsigned DEFAULT NULL, 
  `hall_of_fame_position` smallint unsigned DEFAULT NULL, 
  `played_it_often` tinyint unsigned NOT NULL DEFAULT '0', 
  `ongoing` tinyint unsigned NOT NULL DEFAULT '0', 
  `comments` text, 
  `todo_with_help` tinyint unsigned NOT NULL DEFAULT '0', 
  `bgf` tinyint unsigned NOT NULL DEFAULT '0', 
  `to_watch_position` tinyint unsigned DEFAULT '0', 
  `to_do_position` tinyint unsigned NOT NULL DEFAULT '0') 
  ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
";

$query = $connection->prepare($createStatement);
$query->execute();

# Add unique index on the versions table
$query = $connection->prepare('CREATE UNIQUE INDEX games_platforms ON versions(platform_id, game_id);');
$query->execute();

# Loop on every game
$gamesIndex = [];

$query = $connection->prepare('SELECT * FROM games');
$query->execute();

while ($game = $query->fetch()) {
    msg("Processing game with ID #{$game['id']}");

    $metaQuery = $connection->prepare('SELECT * FROM games_meta WHERE game_id = ' . $game['id']);
    $metaQuery->execute();
    $meta = $metaQuery->fetchAll()[0];

    # Creation of the version and cleaning duplicates
    if (array_key_exists($game['title'], $gamesIndex)) {
        $lastId = insertVersion($gamesIndex[$game['title']], $game['platform'], $meta);
        
        msg("Deleting duplicate {$game['title']}");
        $insertQuery = $connection->prepare("DELETE FROM games WHERE id = {$game['id']}");
        $insertQuery->execute();
        $insertQuery->closeCursor();

    } else {
        $lastId = insertVersion($game['id'], $game['platform'], $meta);
        $gamesIndex[$game['title']] = $game['id'];
    }

    # Updating history
    $updateQuery = $connection->prepare("UPDATE stories SET version_id = $lastId WHERE version_id = {$game['id']}");
    $updateQuery->execute();
}

# Deleting meta
$connection->exec('DROP TABLE games_meta;');

# Remove the platform field in the games table
$query = $connection->prepare('ALTER TABLE games DROP COLUMN platform;');
$query->execute();

# Add unique index on the platform name
$query = $connection->prepare('CREATE UNIQUE INDEX platforms_name ON platforms(name);');
$query->execute();

# Add unique index on the game title
$query = $connection->prepare('CREATE UNIQUE INDEX game_title ON games(title);');
$query->execute();

# Create the table copies
$createStatement = "
CREATE TABLE IF NOT EXISTS copies(
  `copy_id` SMALLINT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
  `version_id` SMALLINT(11) UNSIGNED NOT NULL,
  `type` tinyint unsigned NOT NULL, 
  `box_type` tinyint unsigned NOT NULL, 
  `casing` tinyint unsigned NOT NULL, 
  `on_compilation` tinyint unsigned NOT NULL DEFAULT '0',
  `reedition` tinyint unsigned NOT NULL DEFAULT '0',
  `has_manual` tinyint unsigned NOT NULL DEFAULT '0',
  `comments` text,
  KEY `version_id` (`version_id`),
  CONSTRAINT `copies_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`)
  )ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
";

$connection->exec($createStatement);

# Dump trade table and creates a new one
$connection->exec('DROP TABLE trades;');

$createStatement = "CREATE TABLE `trades` (
    `trade_id` int unsigned NOT NULL AUTO_INCREMENT,
    `copy_id` smallint unsigned NOT NULL,
    `year` smallint unsigned NOT NULL,
    `month` smallint unsigned NOT NULL,
    `day` smallint unsigned NOT NULL,
    `type` tinyint unsigned NOT NULL,
    PRIMARY KEY (`trade_id`),
    KEY `copy_id` (`copy_id`),
    CONSTRAINT `trades_ibfk_1` FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci";

$connection->exec($createStatement);

# Setting back missing FK
$connection->exec("ALTER TABLE stories ADD FOREIGN KEY (version_id) REFERENCES versions(version_id);");
$connection->exec("ALTER TABLE versions ADD FOREIGN KEY (platform_id) REFERENCES platforms(id);");
$connection->exec("ALTER TABLE versions ADD FOREIGN KEY (game_id) REFERENCES games(id);");
