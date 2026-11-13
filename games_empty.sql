-- Adminer 5.4.2 MySQL 8.0.41-0ubuntu0.20.04.1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `copies`;
CREATE TABLE `copies` (
  `copy_id` int unsigned NOT NULL AUTO_INCREMENT,
  `version_id` int unsigned NOT NULL,
  `is_original` tinyint unsigned NOT NULL,
  `language` varchar(255) NOT NULL,
  `box_type` varchar(255) NOT NULL,
  `is_box_repro` tinyint unsigned NOT NULL DEFAULT '0',
  `casing_type` varchar(255) NOT NULL,
  `support_type` varchar(255) NOT NULL,
  `on_compilation` tinyint unsigned NOT NULL,
  `is_reedition` tinyint unsigned NOT NULL,
  `has_manual` tinyint unsigned NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT 'In',
  `type` varchar(255) NOT NULL,
  `region` varchar(255) NOT NULL,
  `is_rom` tinyint unsigned NOT NULL DEFAULT '0',
  `comments` text,
  PRIMARY KEY (`copy_id`),
  KEY `version_id` (`version_id`),
  CONSTRAINT `copies_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `game_version_categories`;
CREATE TABLE `game_version_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `game_version_category_association`;
CREATE TABLE `game_version_category_association` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `version_id` int unsigned NOT NULL,
  `notes` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_category_version` (`category_id`,`version_id`),
  KEY `version_id` (`version_id`),
  CONSTRAINT `game_version_category_association_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `game_version_categories` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `game_version_category_association_ibfk_2` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `game_version_magazine_mentions`;
CREATE TABLE `game_version_magazine_mentions` (
  `mention_id` int unsigned NOT NULL AUTO_INCREMENT,
  `magazine_issue_id` int unsigned NOT NULL,
  `game_version_id` int unsigned NOT NULL,
  `type` varchar(255) NOT NULL,
  `page_number` int unsigned NOT NULL,
  `notes` text,
  PRIMARY KEY (`mention_id`),
  KEY `fk_mention_magazine_issue` (`magazine_issue_id`),
  KEY `fk_mention_game_version` (`game_version_id`),
  CONSTRAINT `fk_mention_game_version` FOREIGN KEY (`game_version_id`) REFERENCES `versions` (`version_id`),
  CONSTRAINT `fk_mention_magazine_issue` FOREIGN KEY (`magazine_issue_id`) REFERENCES `magazine_issues` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `games`;
CREATE TABLE `games` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT '',
  `notes` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `game_title` (`title`),
  KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `magazine_issue_copies`;
CREATE TABLE `magazine_issue_copies` (
  `copy_id` int unsigned NOT NULL AUTO_INCREMENT,
  `magazine_issue_id` int unsigned NOT NULL,
  `type` varchar(255) NOT NULL,
  `notes` text,
  PRIMARY KEY (`copy_id`),
  KEY `fk_magazine_issue_copy_issue` (`magazine_issue_id`),
  CONSTRAINT `fk_magazine_issue_copy_issue` FOREIGN KEY (`magazine_issue_id`) REFERENCES `magazine_issues` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `magazine_issues`;
CREATE TABLE `magazine_issues` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `magazine_id` int unsigned NOT NULL,
  `issue_number` smallint unsigned NOT NULL,
  `year` smallint unsigned NOT NULL,
  `month` tinyint unsigned NOT NULL,
  `notes` text,
  PRIMARY KEY (`id`),
  KEY `fk_magazine_issue_magazine` (`magazine_id`),
  CONSTRAINT `fk_magazine_issue_magazine` FOREIGN KEY (`magazine_id`) REFERENCES `magazines` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `magazines`;
CREATE TABLE `magazines` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `notes` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `notes`;
CREATE TABLE `notes` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text,
  `game_version_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `game_version_id` (`game_version_id`),
  CONSTRAINT `notes_ibfk_1` FOREIGN KEY (`game_version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `platforms`;
CREATE TABLE `platforms` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `platforms_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `stories`;
CREATE TABLE `stories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `version_id` int unsigned DEFAULT NULL,
  `year` smallint unsigned NOT NULL,
  `position` smallint unsigned NOT NULL,
  `watched` tinyint unsigned NOT NULL DEFAULT '0',
  `played` tinyint unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `game_id` (`version_id`),
  CONSTRAINT `stories_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `trades`;
CREATE TABLE `trades` (
  `trade_id` int unsigned NOT NULL AUTO_INCREMENT,
  `copy_id` int unsigned NOT NULL,
  `year` smallint unsigned NOT NULL,
  `month` smallint unsigned NOT NULL,
  `day` smallint unsigned NOT NULL,
  `type` varchar(255) NOT NULL,
  `notes` text,
  PRIMARY KEY (`trade_id`),
  KEY `copy_id` (`copy_id`),
  CONSTRAINT `trades_ibfk_1` FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `transactions`;
CREATE TABLE `transactions` (
  `transaction_id` int unsigned NOT NULL AUTO_INCREMENT,
  `version_id` int unsigned NOT NULL,
  `copy_id` int unsigned DEFAULT NULL,
  `year` smallint unsigned NOT NULL,
  `month` smallint unsigned NOT NULL,
  `day` smallint unsigned NOT NULL,
  `type` varchar(255) NOT NULL,
  `notes` text,
  PRIMARY KEY (`transaction_id`),
  KEY `copy_id` (`copy_id`),
  KEY `transactions_ibfk_2` (`version_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `password` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `salt` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `status` tinyint unsigned NOT NULL DEFAULT '0',
  `user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_2` (`email`),
  UNIQUE KEY `username` (`user_name`),
  KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `versions`;
CREATE TABLE `versions` (
  `version_id` int unsigned NOT NULL AUTO_INCREMENT,
  `platform_id` tinyint unsigned NOT NULL,
  `game_id` int unsigned NOT NULL,
  `release_year` smallint NOT NULL DEFAULT '0',
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
  `to_do_position` tinyint unsigned NOT NULL DEFAULT '0',
  `finished` tinyint unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`version_id`),
  UNIQUE KEY `games_platforms` (`platform_id`,`game_id`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `versions_ibfk_1` FOREIGN KEY (`platform_id`) REFERENCES `platforms` (`id`),
  CONSTRAINT `versions_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2026-08-20 13:42:38 UTC
