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
  `type` tinyint unsigned NOT NULL,
  `box_type` tinyint unsigned NOT NULL,
  `casing` tinyint unsigned NOT NULL,
  `on_compilation` tinyint unsigned NOT NULL DEFAULT '0',
  `reedition` tinyint unsigned NOT NULL DEFAULT '0',
  `has_manual` tinyint unsigned NOT NULL DEFAULT '0',
  `comments` text,
  PRIMARY KEY (`copy_id`),
  KEY `version_id` (`version_id`),
  CONSTRAINT `copies_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copies`
--

LOCK TABLES `copies` WRITE;
/*!40000 ALTER TABLE `copies` DISABLE KEYS */;
INSERT INTO `copies` VALUES (1,349,3,2,4,1,2,3,'Great copy');
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `game_title` (`title`),
  KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=381 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (37,'007 Le monde ne suffit pas'),(43,'1080° Snowboarding'),(146,'688 Sumarine'),(135,'A-10 Tank Killer'),(138,'A10-II Silent Thunder'),(264,'Ace Ventura'),(147,'Aces High'),(133,'Aces of the Pacific'),(132,'Aces over Europe'),(200,'Age of Empires Gold'),(107,'Age of Empires II'),(108,'Age Of Empires II The Conquerors'),(161,'Age Of Empires III'),(163,'Age Of Empires III Asian Dynasties'),(162,'Age Of Empires III Warchiefs'),(190,'Alice Madness Returns'),(257,'Alone in the dark'),(354,'Alone in the Dark 2: One eyed Jack\'s Revenge'),(307,'Alone in the Dark 3 '),(308,'Alone in the Dark: The New Nightmare'),(339,'American McGee\'s Alice'),(373,'Anno 1602'),(279,'Another World'),(270,'Atlantis'),(351,'Atlantis II'),(371,'Aztec'),(269,'Back to the Future: The Game'),(95,'Band Hero'),(362,'Beavis and Butt-Head in Virtual Stupidity'),(356,'Beetle Adventures Racing'),(219,'Beetle Crazy Cup'),(255,'Black and White'),(186,'Black And White 2'),(284,'Blade Runner'),(253,'Bloodmoon (Extension Morrowind)'),(325,'Broken Sword 3: The Sleeping Dragon'),(326,'Broken Sword 4: The Angel of Death'),(327,'Broken Sword 5: The Serpent\'s Curse'),(14,'Bug'),(150,'Caesar 2'),(322,'Caesar 3'),(119,'Carmageddon'),(120,'Carmageddon 2'),(273,'Chicago 1930'),(338,'Chine intrigue dans la cité interdite'),(9,'ClockWork Knight'),(2,'Columns'),(126,'Combat Flight Simulator'),(258,'Combat Flight Simulator 2'),(137,'Command Aces of the Deep'),(110,'Commandos II'),(114,'Commandos: Derrière les lignes ennemies'),(115,'Commandos: Le sens du devoir'),(52,'Confict Zone'),(224,'Conker\'s Bad Fur Day'),(180,'Constructor'),(372,'Cossacks'),(31,'Crash Bandicoot 3'),(62,'Crash Bandicoot: La vengeance de Cortex'),(177,'Crazy Taxi'),(375,'Croc: legend of the gobbos'),(232,'Daria'),(310,'Dark Earth'),(13,'Daytona USA'),(97,'Démonts et Manants'),(195,'Descent'),(214,'Desperados I : Wanted Dead or Alive'),(312,'Desperados II: Western Commandos : La Revanche de Cooper'),(314,'Desperados III'),(313,'Desperados: Helldorado'),(148,'Destroyer Simulation'),(377,'Destruction Derby'),(363,'Deus ex'),(19,'Die Hard Trilogy'),(271,'Dino Crisis'),(259,'Dino Crisis 2'),(89,'Disaster day of crisis'),(201,'Discworld'),(202,'Discworld 2'),(361,'Discworld noir'),(359,'Donkey Kong 64'),(358,'Donkey Kong Country'),(94,'Donkey Kong Country Returns'),(83,'Donkey Konga 2'),(290,'Dracula'),(179,'Dracula 2'),(152,'Dreadnough'),(17,'Driver'),(18,'Driver 2'),(276,'Dune'),(170,'Dust A tale in the wired west'),(239,'Ecstatica 2'),(141,'Egypte 1'),(337,'Egypte II'),(93,'Epic Mickey'),(79,'Eternal Darkness'),(54,'Evolution the world of sacred device'),(125,'F22 Lighting II'),(59,'F355 Challenge'),(275,'Fallout'),(369,'Faust'),(352,'Fifa 11'),(348,'Fifa 2000'),(29,'Fifa 97'),(27,'Fifa 98'),(376,'Fifa 99'),(7,'Fifa Soccer 96'),(208,'Fighting Steel'),(10,'Firestorm Thunderhawk 2'),(380,'Flight Simulator 2000'),(233,'Football Manager 2005'),(171,'Football Manager 96/97'),(222,'Football Manager 98/99'),(117,'Frankeinstein The Eyes of the Monster'),(251,'Gabriel Knight I: Sins of The Father'),(102,'Gabriel Knight II: The Beast Whithin'),(267,'Gabriel Knight III: Blood of the Sacred, Blood of the Damned'),(234,'Gobliiins'),(281,'Gobliins 2: The Prince Buffoon'),(282,'Goblins Quest 3'),(40,'Goldeneye'),(20,'Gran Turismo II'),(164,'Grim Fandango'),(153,'Half Life'),(166,'Hitman'),(154,'Holiday Island'),(100,'IL2 Sturmovik'),(262,'Indiana Jones and the fate of Atlantis'),(283,'Indiana Jones and the last crusade'),(344,'Indiana Jones et la Machine Infernale'),(112,'Iznogoud'),(333,'Jack and Daxter'),(305,'Jack in the Dark'),(265,'Kursk'),(243,'L\'Amerzone'),(144,'Le bouclier de Quetzacoatl (Broken sword II)'),(69,'Le monde des bleus 2002'),(172,'Le trésor du San Diego'),(245,'Leisure Suit Larry I: in the Land of the Lounge Lizards'),(291,'Leisure Suit Larry II: Goes Looking for Love (in Several Wrong Places)'),(292,'Leisure Suit Larry III: Passionate Patti in Pursuit of the Pulsating Pectorals'),(293,'Leisure Suit Larry V: Passionate Patti Does a Little Undercover Work'),(294,'Leisure Suit Larry VI: Shape Up or Slip Out!'),(295,'Leisure Suit Larry VII: Love for Sail!'),(297,'Leisure Suit Larry: Box Office Bust'),(296,'Leisure Suit Larry: Magna Cum Laude'),(298,'Leisure Suit Larry: Reloaded'),(299,'Leisure Suit Larry: Wet Dreams Don\'t Dry'),(203,'Lemmings Revolution'),(145,'Les chevaliers de Baphomet (Broken Sword 1)'),(199,'Les cochons de guerre'),(86,'Les lapins crétins: retour vers le passé'),(28,'Les Razmokets'),(309,'Les Visiteurs : le jeu'),(198,'Les Visiteurs: la relique de Sainte Rolande'),(38,'Little Big Adventure'),(130,'Little Big Adventure 2'),(155,'Liverpool FC'),(277,'Loom'),(334,'Lost Horizon'),(350,'Luigi\'s Mansion'),(207,'Mafia'),(184,'Mafia 2'),(123,'Marine Malice et le Mystère des graines d\'algues'),(45,'Mario 64'),(46,'Mario Golf'),(48,'Mario Kart 64'),(81,'Mario Kart Double Dash'),(85,'Mario Kart Wii'),(76,'Mario Party 5'),(47,'Mario Tennis'),(315,'Max Payne'),(33,'Medal Of Honor'),(187,'Medal Of Honor Allied Assault'),(104,'Medal Of Honor l\'Offensive'),(32,'Medal Of Honor Resistance'),(129,'Medal Of Honor Spearhead'),(24,'Medievil'),(25,'Metal Gear Solid'),(167,'Metal Rage'),(236,'Midtown Madness'),(237,'Midtown Madness 2'),(156,'Monkey Island II'),(140,'Monkey Island III'),(139,'Monkey Island IV'),(181,'Morrowind'),(225,'Myst'),(288,'Myst II : Riven'),(289,'Myst III - Exile'),(319,'Myst IV: Revelation'),(78,'NBA Courtside 2002'),(197,'Need For Speed III'),(196,'Need For Speed V'),(250,'Nibiru : age of secrets'),(209,'Oblivion'),(240,'Pandemonium'),(241,'Pandemonium 2'),(374,'Panzer Commander'),(316,'Panzer General II'),(263,'Paradise'),(345,'Parasite Eve'),(335,'Paris 1313 le disparu de notre dame'),(165,'Phantasmagoria'),(256,'Phantasmagoria : obsessions fatales'),(323,'Pharaon'),(370,'Pilgrim'),(355,'Pilot Wings'),(105,'Pirates'),(286,'Pompei'),(142,'Power Chess'),(300,'Pro Evolution Soccer'),(64,'Pro Evolution Soccer 2'),(111,'Pro Evolution Soccer 6'),(157,'Project IGI'),(367,'Quest for Glory: Shadows of Darkness'),(341,'Rayman 2: The Great Escape'),(364,'Rayman 3: Hoodlum Havoc'),(304,'Rayman contre les lapins encore + crétins'),(134,'Red Baron'),(127,'Red Baron 3D'),(21,'Resident Evil'),(74,'Resident Evil 0'),(22,'Resident Evil 2'),(23,'Resident Evil 3'),(58,'Resident Evil Code Veronica'),(88,'Resident Evil The Dark Side Chronicle'),(84,'Resident Evil Umbrella Chronicles'),(4,'Revenge Of Shinobi'),(34,'Ridge Racer Type 4'),(128,'Rise of Nations  '),(113,'Rise Of Nations Throne & Patriots'),(321,'Rule the waves II'),(215,'Runaway'),(229,'Runaway 2'),(230,'Runaway 3 '),(261,'Sam and Max'),(204,'Screamer 4x4 Rally'),(11,'Sega Rally'),(169,'Sega Rally 2'),(1,'Sega Soccer'),(36,'Sherif fais moi peur'),(213,'Shivers'),(26,'Silent Hill'),(71,'Silent Hill 2'),(70,'Silent Hill 3'),(68,'Silent Hill 4'),(73,'Silent Hill Origins'),(98,'Silent Hunter II'),(191,'Silent Hunter III'),(185,'Silent Hunter IV'),(223,'Simcity 2000'),(368,'Simcity 3000'),(247,'Simon the sorcerer'),(347,'Soccer'),(5,'Sonic'),(50,'Sonic Adventure'),(349,'Sonic R'),(378,'Soviet Strike'),(343,'Space Station Silicon Valley'),(53,'Speed Devils'),(182,'Splinter Cell'),(116,'SPQR'),(192,'Star Wars Knights Of The Old Republic'),(311,'Star Wars racer'),(342,'Star Wars: Episode I Battle for Naboo'),(121,'Starcraft'),(99,'Starcraft Brood War'),(6,'Streets of Rage'),(87,'Super Mario Bros Wii'),(252,'Super Mario Land 2'),(3,'Super Monaco GP'),(92,'Super Smash Bros Brawl'),(80,'Super Smash Bros Melee'),(366,'Swat 2'),(193,'Syberia'),(211,'Syberia 2'),(231,'Syberia 3'),(328,'Tales of Monkey Island: chapter 1'),(329,'Tales of Monkey Island: chapter 2 The siege of spinner cay'),(330,'Tales of Monkey Island: chapter 3: lair of the leviathan'),(331,'Tales of Monkey Island: chapter 4: the trial and execution of Guybrush Threepwood'),(332,'Tales of Monkey Island: chapter 5: rise of the pirate god'),(39,'Tekken 3'),(72,'Tekken 5'),(61,'Tekken Tag'),(136,'The aviation pionneers'),(249,'The day of the tentacle'),(90,'The Dead Rising'),(246,'The dig'),(101,'The FullThrottle'),(160,'The Last Express'),(346,'The Legend of Zelda: A Link to the Past'),(360,'The Settlers II'),(106,'The Settlers II - Tenth anniversary edition'),(175,'The X Files'),(205,'Theme Hospital'),(260,'Thimbleweed Park'),(176,'Titanic un voyage interactif'),(96,'Titanic: An Adventure Out Of Time'),(8,'Tomb Raider'),(122,'Tomb Raider II'),(220,'Tomb Raider III'),(159,'Tomb Raider IV'),(287,'Tomb Raider V'),(379,'Tonic Trouble'),(178,'Tout le bridge aujourd\'hui'),(158,'Transport Tycoon Deluxe'),(210,'Tribunal (ext. Morrowind)'),(56,'Trick Style'),(218,'Trine 1'),(217,'Trine 2'),(189,'Un voisin d\'enfer'),(320,'Uru: ages beyond Myst'),(51,'V-Rally 2  Expert Edition'),(30,'V-Rally 97 Championship Edition'),(188,'Versailles'),(174,'Versailles II'),(60,'Vigilant 8 2nd Offense'),(301,'Vigilante 8'),(16,'Virtua Cop 2'),(183,'Virtua Tennis'),(168,'Virtua Tennis 3'),(194,'Virtual Pool'),(149,'Warbird 2'),(274,'Warcraft Adventures'),(285,'Warcraft II'),(91,'Wii Sports'),(35,'Wing Over'),(206,'Woodruff'),(44,'World Cup 98'),(15,'Worlwide Soccer 97'),(143,'Worms Armagueddon'),(124,'Worms Fort Etat de Siège'),(340,'WWII Online'),(248,'Yesterday Origins'),(357,'Yoshi\'s Island'),(49,'Yoshi\'s Story'),(42,'Zelda Majora\'s Mask'),(41,'Zelda Ocarina Of Time'),(82,'Zelda Twilight Princess'),(75,'Zelda WindWaker');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platforms`
--

LOCK TABLES `platforms` WRITE;
/*!40000 ALTER TABLE `platforms` DISABLE KEYS */;
INSERT INTO `platforms` VALUES (9,'Dreamcast'),(10,'Game Boy'),(5,'GameCube'),(7,'Megadrive II'),(4,'Nintendo 64'),(1,'PC'),(2,'Playstation'),(3,'Playstation 2'),(8,'Saturn'),(11,'Super Nintendo'),(6,'Wii');
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
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stories`
--

LOCK TABLES `stories` WRITE;
/*!40000 ALTER TABLE `stories` DISABLE KEYS */;
INSERT INTO `stories` VALUES (2,231,2018,1,1,0),(3,95,2018,2,1,0),(4,40,2019,1,1,0),(5,248,2019,3,1,0),(6,41,2019,4,1,0),(7,238,2019,5,1,0),(8,68,2019,6,1,0),(11,247,2020,2,1,0),(13,114,2020,5,1,0),(14,207,2020,8,1,0),(15,149,2020,9,1,0),(16,261,2020,7,1,0),(17,210,2020,1,1,0),(18,132,2020,10,1,0),(19,245,2020,11,1,0),(20,55,2020,12,1,0),(21,20,2021,1,1,0),(22,225,2021,2,1,0),(23,265,2021,3,1,0),(25,21,2021,4,1,0),(27,257,2020,3,1,0),(29,211,2020,13,1,0),(30,262,2020,14,1,0),(31,263,2020,15,1,0),(32,235,2020,16,1,0),(33,260,2021,5,1,0),(35,214,2020,4,1,0),(36,289,2020,18,0,1),(37,24,2017,1,1,0),(38,266,2021,6,1,0),(39,230,2021,7,1,0),(40,98,2021,9,0,1),(41,190,2019,7,1,0),(43,264,2021,8,1,0),(44,227,2021,10,1,0),(45,252,2021,11,1,0),(46,168,2021,12,1,0),(47,195,2021,13,1,0),(48,108,2020,6,1,0),(49,22,2021,14,1,0),(50,37,2021,15,1,0),(51,283,2021,16,1,0),(52,177,2021,17,0,1),(53,164,2021,18,1,0),(54,282,2021,19,0,1),(55,122,2021,20,1,0),(56,309,2021,21,1,0),(57,267,2021,22,1,0),(58,131,2021,24,0,1),(59,292,2019,2,0,1),(60,186,2020,17,0,1),(61,268,2021,25,1,0),(62,310,2021,23,0,1),(63,8,2021,26,1,1),(64,314,2021,27,1,0),(66,325,2021,28,0,1),(67,107,2021,29,0,1),(68,236,2021,30,1,0),(69,243,2019,1,1,0),(70,315,2021,32,1,0),(71,245,2021,33,1,0),(72,204,2020,19,0,1),(73,204,2021,34,0,1),(74,324,2022,1,1,0),(75,244,2018,3,0,1),(76,321,2022,2,1,0),(77,106,2022,3,0,1),(78,204,2022,4,1,1),(79,269,2022,5,1,0),(80,280,2022,6,1,0),(82,191,2022,7,1,0),(83,331,2022,8,1,0),(84,87,2021,35,0,1),(85,87,2022,9,1,1),(86,90,2022,10,0,1),(87,241,2022,11,1,0),(88,338,2022,12,1,0),(89,80,2022,13,0,1),(90,224,2022,14,0,1);
/*!40000 ALTER TABLE `stories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trades`
--

DROP TABLE IF EXISTS `trades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trades` (
  `trade_id` int unsigned NOT NULL AUTO_INCREMENT,
  `copy_id` smallint unsigned NOT NULL,
  `year` smallint unsigned NOT NULL,
  `month` smallint unsigned NOT NULL,
  `day` smallint unsigned NOT NULL,
  `type` tinyint unsigned NOT NULL,
  PRIMARY KEY (`trade_id`),
  KEY `copy_id` (`copy_id`),
  CONSTRAINT `trades_ibfk_1` FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trades`
--

LOCK TABLES `trades` WRITE;
/*!40000 ALTER TABLE `trades` DISABLE KEYS */;
/*!40000 ALTER TABLE `trades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'foo@bar.com','yhh1dbdhtr57b6htrhb8n845v69c4tr9v3q456bdbhtyhcafb8d','TfrWefrAk',1,'Eric','tokentest123');
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
  PRIMARY KEY (`version_id`),
  UNIQUE KEY `games_platforms` (`platform_id`,`game_id`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `versions_ibfk_1` FOREIGN KEY (`platform_id`) REFERENCES `platforms` (`id`),
  CONSTRAINT `versions_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `games` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=350 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `versions`
--

LOCK TABLES `versions` WRITE;
/*!40000 ALTER TABLE `versions` DISABLE KEYS */;
INSERT INTO `versions` VALUES (1,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(2,7,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(3,7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(4,7,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(5,7,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(6,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(7,7,7,0,0,0,0,0,0,0,0,0,0,0,1,1996,1,1,0,NULL,0,0,0,0),(8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(10,8,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(11,8,11,0,1,0,0,0,0,0,0,0,0,0,1,1998,8,1,0,NULL,0,0,0,0),(12,8,13,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(13,8,14,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(14,8,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(15,8,16,0,0,0,0,0,0,0,0,0,0,0,1,1998,7,1,0,NULL,0,0,0,0),(16,2,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(17,2,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(18,2,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(19,2,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(20,2,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(21,2,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(22,2,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(23,2,24,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,8),(24,2,25,0,0,0,0,0,0,0,0,0,1,1,1,1999,4,0,0,NULL,0,1,0,0),(25,2,26,0,0,0,0,0,0,0,0,0,1,1,1,2001,3,0,0,NULL,0,0,0,0),(26,2,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(27,2,28,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(28,2,29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(29,2,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(30,2,31,0,0,0,0,0,0,0,0,0,0,0,1,2000,3,0,0,NULL,0,0,0,0),(31,2,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(32,2,33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(33,2,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(34,2,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(35,2,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(36,2,37,0,0,0,0,0,0,0,0,0,1,0,1,2000,5,0,0,NULL,0,0,0,0),(37,2,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(38,2,39,0,0,0,0,0,0,0,0,0,0,0,1,2000,6,1,0,NULL,0,0,0,0),(39,4,40,0,0,1,0,0,0,0,0,0,0,0,1,1997,2,1,0,NULL,0,0,0,0),(40,4,41,0,0,0,0,0,0,0,0,0,0,1,1,1999,2,0,0,NULL,0,1,0,0),(41,4,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(42,4,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(43,4,44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(44,4,45,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(45,4,46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(46,4,47,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(47,4,48,0,0,1,0,0,0,0,0,0,0,1,1,1998,6,1,0,NULL,0,1,0,0),(48,4,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(49,9,50,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(50,9,51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(51,9,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(52,9,53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(53,9,54,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(54,9,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(55,9,58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(56,9,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(57,9,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(58,3,61,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(59,3,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(60,3,64,0,0,1,0,0,0,0,0,0,0,0,1,2002,4,1,0,NULL,0,0,0,0),(61,3,68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(62,3,69,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(63,3,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(64,3,71,0,0,0,0,0,0,0,0,0,1,1,1,2001,4,0,0,NULL,0,1,0,0),(65,3,72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(66,3,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(67,5,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(68,5,75,0,0,0,0,0,0,0,0,0,0,0,1,2004,5,0,0,NULL,0,0,0,0),(69,5,76,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(70,5,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(71,5,78,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(72,5,79,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,3),(73,5,80,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(74,5,81,0,0,1,0,0,0,0,0,0,0,0,1,2003,3,1,0,NULL,0,0,0,0),(75,5,82,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(76,5,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(77,6,84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(78,6,85,0,0,1,0,0,0,0,0,0,0,0,1,2008,1,1,0,NULL,0,0,0,0),(79,6,86,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(80,6,87,0,1,1,0,0,0,0,0,0,0,1,1,2022,5,0,0,NULL,0,0,0,0),(81,6,88,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(82,6,89,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(83,6,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(84,6,91,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(85,6,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(86,6,93,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(87,6,94,0,1,1,0,0,0,0,0,0,0,0,1,2021,5,0,0,NULL,0,0,0,0),(88,6,95,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(89,1,96,0,0,0,0,0,1,0,0,0,0,1,1,1998,1,1,0,NULL,0,1,0,10),(90,1,97,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(91,1,98,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(92,1,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(93,1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(94,1,101,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(95,1,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(96,1,104,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(97,1,105,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(98,1,106,0,0,0,1,0,0,0,0,0,0,0,1,2007,2,0,0,NULL,1,0,0,0),(99,1,107,0,0,0,0,0,0,0,0,0,0,1,1,1999,6,1,0,NULL,0,0,0,0),(100,1,108,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(101,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(102,1,110,0,0,0,0,1,1,0,0,0,0,1,1,2003,2,1,0,NULL,0,1,0,0),(103,1,111,0,0,0,1,1,0,0,0,0,0,1,1,2006,1,0,0,NULL,0,0,0,0),(104,1,112,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(105,1,113,0,0,0,1,1,0,0,0,0,0,1,1,2004,1,1,0,NULL,0,0,0,0),(106,1,114,0,0,0,0,1,0,0,0,0,0,0,1,1999,8,0,1,NULL,0,0,0,0),(107,1,115,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(108,1,116,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(109,1,117,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(110,1,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(111,1,119,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(112,1,120,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(113,1,121,0,0,0,0,0,0,0,0,0,0,0,1,1999,3,1,0,NULL,0,0,0,0),(114,1,122,0,0,0,0,0,1,0,0,0,0,0,1,1998,10,0,0,NULL,0,0,0,6),(115,1,123,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(116,1,124,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(117,1,125,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(118,1,126,0,0,0,1,0,0,0,0,0,0,1,1,2001,2,1,0,NULL,0,0,0,0),(119,1,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(120,1,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(121,1,129,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(122,1,130,0,0,0,0,0,0,0,0,0,1,1,1,1997,1,0,0,NULL,0,1,0,0),(123,1,132,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(124,1,133,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(125,1,134,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(126,1,135,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(127,1,136,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(128,1,137,0,0,0,0,0,0,0,0,0,0,0,1,1999,1,1,0,NULL,0,1,0,0),(129,1,138,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(130,1,139,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(131,1,140,0,0,0,0,0,0,0,0,0,0,1,1,2001,1,1,0,NULL,0,1,0,0),(132,1,141,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(133,1,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(134,1,143,0,0,0,0,1,0,0,0,0,0,1,1,2001,8,1,0,NULL,0,0,0,0),(135,1,144,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(136,1,145,0,0,0,0,0,0,0,0,0,0,1,1,2001,6,0,0,NULL,0,0,0,0),(137,1,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(138,1,147,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(139,1,148,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(140,1,149,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(141,1,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(142,1,152,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(143,1,153,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(144,1,154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(145,1,155,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(146,1,156,0,0,0,0,0,0,0,0,0,0,0,1,2001,5,0,0,NULL,0,0,0,0),(147,1,157,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(148,1,158,0,0,0,1,0,0,0,0,0,0,1,1,1998,3,1,0,NULL,0,1,0,0),(149,1,159,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(150,1,160,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(151,1,161,0,0,0,0,0,0,1,0,0,0,1,1,2005,3,0,0,NULL,0,0,0,0),(152,1,162,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(153,1,163,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(154,1,164,0,0,0,0,0,0,0,0,0,0,0,1,2004,4,0,0,NULL,0,0,0,0),(155,1,165,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(156,1,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(157,1,167,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(158,1,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(159,1,169,0,1,0,0,0,0,0,0,0,0,0,1,2002,6,1,0,NULL,0,0,0,0),(160,1,170,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(161,1,171,0,0,0,0,0,0,0,0,0,0,0,1,1998,2,1,0,NULL,0,0,0,0),(162,1,172,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(163,1,174,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,NULL,1,0,0,0),(164,1,175,0,0,0,0,0,0,0,0,0,0,1,1,2000,1,0,0,NULL,1,0,0,0),(165,1,176,0,0,0,0,0,0,0,0,0,0,0,1,1996,2,0,0,NULL,0,0,0,0),(166,1,177,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(167,1,178,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(168,1,179,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(169,1,180,0,0,0,0,0,1,0,0,0,0,0,1,2001,7,0,0,NULL,1,0,0,13),(170,1,181,0,0,0,1,0,0,0,0,0,0,0,1,2002,1,0,0,NULL,0,1,0,0),(171,1,182,0,0,0,0,0,0,0,0,0,0,0,1,2010,1,0,0,NULL,0,0,0,0),(172,1,183,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(173,1,184,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(174,1,185,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(175,1,186,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(176,1,187,0,0,0,0,1,0,0,0,0,0,0,1,2002,3,1,0,NULL,0,0,0,0),(177,1,188,0,0,0,0,0,0,0,0,0,0,0,1,1999,7,0,0,NULL,1,0,0,0),(178,1,189,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(179,1,190,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(180,1,191,0,0,0,1,1,0,0,0,0,0,1,1,2005,1,1,0,NULL,0,1,0,0),(181,1,192,0,0,0,0,0,0,0,0,0,0,0,1,2005,2,1,0,NULL,0,0,0,0),(182,1,193,0,0,0,0,0,0,0,0,0,0,1,1,2004,2,0,0,NULL,0,0,0,0),(183,1,194,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(184,1,195,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(185,1,196,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(186,1,197,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(187,1,198,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(188,1,199,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(189,1,200,0,0,0,0,0,0,0,0,0,0,1,1,1998,5,1,0,NULL,0,0,0,0),(190,1,201,0,0,0,0,0,0,0,0,0,0,0,1,2012,1,0,0,NULL,0,0,0,0),(191,1,202,0,0,0,0,0,0,0,0,0,0,0,1,2022,3,0,0,NULL,0,0,0,0),(192,1,203,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(193,1,204,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(194,1,205,0,0,0,1,0,0,0,0,0,0,1,1,1998,4,1,0,NULL,0,0,0,0),(195,1,206,0,0,0,0,0,0,0,0,0,0,0,1,1998,8,0,0,NULL,1,0,0,0),(196,1,207,0,1,0,0,0,0,0,0,0,0,1,1,2003,1,1,0,NULL,0,0,0,0),(197,1,208,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,NULL,0,0,0,0),(198,1,209,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(199,1,210,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(200,1,211,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(201,1,213,0,0,0,0,0,0,0,0,0,0,0,1,2022,1,0,0,NULL,0,1,0,0),(202,1,214,0,0,0,0,0,1,0,0,0,0,0,1,2007,1,0,0,NULL,0,0,0,0),(203,1,215,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(204,1,217,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(205,1,218,0,0,0,0,0,0,0,0,0,0,0,1,2009,1,0,0,NULL,0,0,0,0),(206,1,219,0,1,1,0,0,0,0,0,0,0,0,1,2000,4,1,0,NULL,0,0,0,0),(207,1,220,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,99),(208,1,222,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,NULL,0,0,0,0),(209,1,223,0,0,0,1,0,0,0,0,0,0,1,1,1997,3,1,0,NULL,0,0,0,0),(210,4,224,0,0,0,0,0,0,0,0,0,0,1,1,2020,2,0,0,NULL,0,0,0,0),(211,1,225,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,12),(212,1,229,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(213,1,230,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(214,1,231,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(215,1,232,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(216,1,233,0,0,0,0,0,0,0,0,0,0,0,0,2005,4,0,0,NULL,0,0,0,0),(217,1,234,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(218,1,236,0,0,0,0,0,0,0,0,0,0,0,1,2000,2,1,0,NULL,0,0,0,0),(219,1,237,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(220,1,16,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(221,1,239,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(222,1,240,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(223,1,241,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(224,1,243,0,0,0,0,0,0,0,0,0,0,0,1,2022,2,0,0,NULL,0,0,0,0),(225,1,245,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(226,1,246,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(227,1,247,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(228,1,248,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(229,1,249,0,0,0,0,0,0,0,0,0,0,0,1,2004,3,0,0,NULL,0,0,0,0),(230,1,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(231,1,251,0,0,0,0,0,0,0,0,0,1,0,1,2018,1,0,0,NULL,0,1,0,0),(232,10,252,0,0,0,0,0,0,1,0,0,0,1,1,1993,1,1,0,NULL,0,0,0,0),(233,1,253,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(234,1,255,0,0,0,0,0,1,0,0,0,0,0,1,2002,5,0,0,NULL,0,0,0,9),(235,1,256,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(236,1,257,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(237,1,258,0,0,0,1,0,0,0,0,0,0,1,1,2002,5,1,0,NULL,0,0,0,0),(238,2,259,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(239,1,260,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(240,1,261,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(241,1,262,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(242,1,263,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(243,1,264,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(244,1,265,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(245,1,267,0,0,0,0,0,0,0,0,0,1,0,1,2020,3,0,0,NULL,0,0,0,0),(246,1,269,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(247,1,270,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(248,2,271,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(249,1,273,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(250,1,274,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(251,1,275,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(252,1,276,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(253,1,277,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(254,1,279,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(255,1,281,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(256,1,282,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(257,1,283,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(258,1,284,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(259,1,285,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(260,1,286,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(261,2,287,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(262,1,288,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(263,1,289,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(264,1,290,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(265,1,291,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(266,1,292,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(267,1,293,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(268,1,294,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(269,1,295,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(270,1,296,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(271,1,297,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(272,1,298,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(273,1,299,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(274,3,300,0,0,0,0,0,0,0,0,0,0,0,1,2002,2,0,0,NULL,0,0,0,0),(275,4,301,0,0,0,0,0,0,0,0,0,0,0,1,1999,5,0,0,NULL,0,0,0,0),(276,1,29,0,0,0,0,0,0,0,0,0,0,0,1,1997,4,1,0,NULL,0,0,0,0),(277,4,27,0,0,0,0,0,0,0,0,0,0,0,1,1997,4,0,0,NULL,0,0,0,0),(278,6,304,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(279,1,305,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(280,1,307,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(281,9,308,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,8),(282,1,309,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(283,1,310,0,0,0,0,0,0,0,0,0,0,0,1,2021,1,0,0,NULL,0,0,0,0),(284,1,311,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(285,1,312,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(286,1,313,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(287,1,314,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(288,1,315,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(289,1,316,0,0,0,1,1,0,0,0,0,0,1,1,2020,1,1,0,NULL,0,0,0,0),(290,1,319,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(291,1,320,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(292,1,321,0,0,0,1,0,0,0,0,0,0,1,1,2019,1,1,0,NULL,0,0,0,0),(293,1,322,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(294,1,323,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(295,1,325,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(296,1,326,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(297,1,327,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(298,1,328,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(299,1,329,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(300,1,330,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(301,1,331,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(302,1,332,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(303,3,333,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(304,1,334,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(305,1,335,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(306,1,287,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(307,1,337,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(308,1,338,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(309,1,339,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(310,1,340,0,1,0,0,0,0,0,0,0,0,1,1,2006,2,0,0,NULL,0,0,0,0),(311,4,341,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(312,4,342,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(313,4,343,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(314,1,344,0,0,0,0,0,0,0,0,0,0,0,1,2021,3,0,0,NULL,0,0,0,0),(315,2,345,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(316,11,346,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(317,10,347,0,0,0,0,0,0,0,0,0,0,0,1,1996,3,1,0,NULL,0,0,0,0),(318,1,348,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0),(319,1,349,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(320,5,350,0,0,0,0,0,0,0,0,0,0,0,1,2021,2,0,0,NULL,0,0,0,0),(321,1,351,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(322,1,352,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(323,2,240,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,7),(324,2,354,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(325,4,355,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(326,4,356,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(327,11,357,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(328,11,358,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,11),(329,4,359,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(330,1,360,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(331,1,361,0,0,0,0,0,0,0,0,0,0,0,1,2022,4,0,0,NULL,0,0,0,0),(332,1,362,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(333,1,363,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(334,3,364,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(335,1,366,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(336,1,367,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(337,1,368,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(338,1,369,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(339,1,370,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(340,1,371,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0),(341,1,372,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(342,1,373,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0),(343,1,374,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(344,2,375,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(345,1,376,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(346,8,377,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,4),(347,8,378,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,5),(348,1,379,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0),(349,1,380,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0);
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

-- Dump completed on 2022-05-25 08:25:32
