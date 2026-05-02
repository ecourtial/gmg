-- DROP the Foreign keys

-- version_id	versions(version_id)	RESTRICT	RESTRICT
ALTER TABLE `copies` DROP FOREIGN KEY `copies_ibfk_1`;

-- version_id	versions(version_id)	RESTRICT	RESTRICT
ALTER TABLE `stories` DROP FOREIGN KEY `stories_ibfk_1`;

-- copy_id	copies(copy_id)	RESTRICT	RESTRICT
ALTER TABLE `trades` DROP FOREIGN KEY `trades_ibfk_1`;

-- copy_id	copies(copy_id)	RESTRICT	RESTRICT
ALTER TABLE `transactions` DROP FOREIGN KEY `transactions_ibfk_1`;

-- version_id	versions(version_id) RESTRICT	RESTRICT
ALTER TABLE `transactions` DROP FOREIGN KEY `transactions_ibfk_2`;

-- game_id	games(id)	RESTRICT	RESTRICT
ALTER TABLE `versions` DROP FOREIGN KEY `versions_ibfk_2`;

-- UPDATE fields type

ALTER TABLE `games`
CHANGE `id` `id` int unsigned NOT NULL AUTO_INCREMENT FIRST;

ALTER TABLE `copies`
CHANGE `copy_id` `copy_id` int unsigned NOT NULL AUTO_INCREMENT FIRST,
CHANGE `version_id` `version_id` int unsigned NOT NULL AFTER `copy_id`;

ALTER TABLE `trades`
CHANGE `copy_id` `copy_id` int unsigned NOT NULL AFTER `trade_id`;

ALTER TABLE `transactions`
CHANGE `version_id` `version_id` int unsigned NOT NULL AFTER `transaction_id`,
CHANGE `copy_id` `copy_id` int unsigned NULL AFTER `version_id`;

ALTER TABLE `versions`
CHANGE `version_id` `version_id` int unsigned NOT NULL AUTO_INCREMENT FIRST,
CHANGE `game_id` `game_id` int unsigned NOT NULL AFTER `platform_id`;

ALTER TABLE `stories`
CHANGE `version_id` `version_id` int unsigned NULL AFTER `id`;

-- RECREATE foreign keys

ALTER TABLE `copies` ADD FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `stories` ADD FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `trades` ADD FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `transactions` ADD FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `transactions` ADD FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `versions` ADD FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- ADD new tables

CREATE TABLE `magazines` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` TEXT NOT NULL,
  `notes` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `magazine_issues` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `magazine_id` INT UNSIGNED NOT NULL,
  `issue_number` SMALLINT UNSIGNED NOT NULL,
  `year` SMALLINT UNSIGNED NOT NULL,
  `month` TINYINT UNSIGNED NOT NULL,
  `notes` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_magazine_issue_magazine` FOREIGN KEY (`magazine_id`) REFERENCES `magazines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `magazine_issue_copies` (
  `copy_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `magazine_issue_id` INT UNSIGNED NOT NULL,
  `type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`copy_id`),
  CONSTRAINT `fk_magazine_issue_copy_issue` FOREIGN KEY (`magazine_issue_id`) REFERENCES `magazine_issues` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `game_version_magazine_mentions` (
  `mention_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `magazine_issue_id` INT UNSIGNED NOT NULL,
  `game_version_id` INT UNSIGNED NOT NULL,
  `type` VARCHAR(255) NOT NULL,
  `notes` TEXT NOT NULL,
  PRIMARY KEY (`mention_id`),
  CONSTRAINT `fk_mention_magazine_issue` FOREIGN KEY (`magazine_issue_id`) REFERENCES `magazine_issues` (`id`),
  CONSTRAINT `fk_mention_game_version` FOREIGN KEY (`game_version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
