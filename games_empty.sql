# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Hôte: 0.0.0.0 (MySQL 5.7.29)
# Base de données: games
# Temps de génération: 2021-02-16 21:10:11 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Affichage de la table games
# ------------------------------------------------------------

DROP TABLE IF EXISTS `games`;

CREATE TABLE `games` (
  `id` smallint(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT '',
  `platform` tinyint(4) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `support` (`platform`),
  KEY `title` (`title`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`platform`) REFERENCES `platforms` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Affichage de la table games_meta
# ------------------------------------------------------------

DROP TABLE IF EXISTS `games_meta`;

CREATE TABLE `games_meta` (
  `game_id` smallint(11) unsigned NOT NULL AUTO_INCREMENT,
  `todo_solo_sometimes` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `todo_multiplayer_sometimes` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `singleplayer_recurring` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `multiplayer_recurring` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `to_do` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `to_buy` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `to_watch_background` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `to_watch_serious` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `to_rewatch` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `original` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `copy` tinyint(1) unsigned NOT NULL,
  `many` tinyint(1) unsigned NOT NULL,
  `top_game` tinyint(1) unsigned NOT NULL,
  `hall_of_fame` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `hall_of_fame_year` smallint(11) unsigned DEFAULT NULL,
  `hall_of_fame_position` smallint(11) unsigned DEFAULT NULL,
  `played_it_often` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `ongoing` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `comments` text,
  `todo_with_help` tinyint(3) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`game_id`),
  CONSTRAINT `games_meta_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Affichage de la table history
# ------------------------------------------------------------

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `game_id` smallint(11) unsigned NOT NULL,
  `year` smallint(6) NOT NULL,
  `position` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `history_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Affichage de la table platforms
# ------------------------------------------------------------

DROP TABLE IF EXISTS `platforms`;

CREATE TABLE `platforms` (
  `id` tinyint(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Affichage de la table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `password` tinytext CHARACTER SET utf8mb4 NOT NULL,
  `salt` varchar(20) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `status` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `user_name` varchar(255) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_2` (`email`),
  UNIQUE KEY `username` (`user_name`),
  KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
