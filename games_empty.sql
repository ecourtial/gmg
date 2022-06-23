-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: games
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `copies`
--

DROP TABLE IF EXISTS `copies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `copies` (
  `copy_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `version_id` smallint unsigned NOT NULL,
  `is_original` tinyint unsigned NOT NULL,
  `language` varchar(255) NOT NULL,
  `box_type` varchar(255) NOT NULL,
  `casing_type` varchar(255) NOT NULL,
  `support_type` varchar(255) NOT NULL,
  `on_compilation` tinyint unsigned NOT NULL,
  `is_reedition` tinyint unsigned NOT NULL,
  `has_manual` tinyint unsigned NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT 'In',
  `type` varchar(255) NOT NULL,
  `comments` text,
  PRIMARY KEY (`copy_id`),
  KEY `version_id` (`version_id`),
  CONSTRAINT `copies_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copies`
--

LOCK TABLES `copies` WRITE;
/*!40000 ALTER TABLE `copies` DISABLE KEYS */;
/*!40000 ALTER TABLE `copies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT '',
  `notes` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `game_title` (`title`),
  KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platforms`
--

DROP TABLE IF EXISTS `platforms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platforms` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `platforms_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platforms`
--

LOCK TABLES `platforms` WRITE;
/*!40000 ALTER TABLE `platforms` DISABLE KEYS */;
/*!40000 ALTER TABLE `platforms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stories`
--

DROP TABLE IF EXISTS `stories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `version_id` smallint unsigned DEFAULT NULL,
  `year` smallint unsigned NOT NULL,
  `position` smallint unsigned NOT NULL,
  `watched` tinyint unsigned NOT NULL DEFAULT '0',
  `played` tinyint unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `game_id` (`version_id`),
  CONSTRAINT `stories_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stories`
--

LOCK TABLES `stories` WRITE;
/*!40000 ALTER TABLE `stories` DISABLE KEYS */;
/*!40000 ALTER TABLE `stories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` int unsigned NOT NULL AUTO_INCREMENT,
  `version_id` smallint unsigned NOT NULL,
  `copy_id` smallint unsigned DEFAULT NULL,
  `year` smallint unsigned NOT NULL,
  `month` smallint unsigned NOT NULL,
  `day` smallint unsigned NOT NULL,
  `type` varchar(255) NOT NULL,
  `notes` text,
  PRIMARY KEY (`transaction_id`),
  KEY `copy_id` (`copy_id`),
  KEY `transactions_ibfk_2` (`version_id`),
  CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`),
  CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `password` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `salt` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `status` tinyint unsigned NOT NULL DEFAULT '0',
  `user_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `token` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_2` (`email`),
  UNIQUE KEY `username` (`user_name`),
  KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'foo@bar.com','802cee6fdb8f3964700a7d789bd034cee6e5dba100f2c3df1fcb2b9afdc97b2b','kK0pXVUq',1,'foo','tokentest123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `versions`
--

DROP TABLE IF EXISTS `versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `versions` (
  `version_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `platform_id` tinyint unsigned NOT NULL,
  `game_id` smallint unsigned NOT NULL,
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
  CONSTRAINT `versions_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `versions`
--

LOCK TABLES `versions` WRITE;
/*!40000 ALTER TABLE `versions` DISABLE KEYS */;
/*!40000 ALTER TABLE `versions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-23 14:36:45
