-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: games
-- ------------------------------------------------------
-- Server version	8.0.32

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
  CONSTRAINT `copies_ibfk_1` FOREIGN KEY (`version_id`) REFERENCES `versions` (`version_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copies`
--

LOCK TABLES `copies` WRITE;
/*!40000 ALTER TABLE `copies` DISABLE KEYS */;
INSERT INTO `copies` VALUES (1,348,1,'fr','Big box',0,'CD-like','CD-ROM',0,0,1,'In','Physical','PAL',0,'Bought it in 2004'),(2,349,1,'fr','none',0,'Cardboard sleeve','CD-ROM',1,1,0,'In','Physical','PAL',0,'Got it with my cereals'),(3,245,1,'fr','None',0,'CD-like','CD-ROM',1,1,0,'In','Physical','PAL',0,'pues');
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
) ENGINE=InnoDB AUTO_INCREMENT=381 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'Sega Soccer','super jeu !!!'),(2,'Columns','bof bof'),(3,'Super Monaco GP',NULL),(4,'Revenge Of Shinobi',NULL),(5,'Sonic',NULL),(6,'Streets of Rage',NULL),(7,'Fifa Soccer 96',NULL),(8,'Tomb Raider',NULL),(9,'ClockWork Knight',NULL),(10,'Firestorm Thunderhawk 2',NULL),(11,'Sega Rally',NULL),(13,'Daytona USA',NULL),(14,'Bug',NULL),(15,'Worlwide Soccer 97',NULL),(16,'Virtua Cop 2',NULL),(17,'Driver',NULL),(18,'Driver 2',NULL),(19,'Die Hard Trilogy',NULL),(20,'Gran Turismo II',NULL),(21,'Resident Evil',NULL),(22,'Resident Evil 2',NULL),(23,'Resident Evil 3',NULL),(24,'Medievil',NULL),(25,'Metal Gear Solid',NULL),(26,'Silent Hill',NULL),(27,'Fifa 98',NULL),(28,'Les Razmokets',NULL),(29,'Fifa 97',NULL),(30,'V-Rally 97 Championship Edition',NULL),(31,'Crash Bandicoot 3',NULL),(32,'Medal Of Honor Resistance',NULL),(33,'Medal Of Honor',NULL),(34,'Ridge Racer Type 4',NULL),(35,'Wing Over',NULL),(36,'Sherif fais moi peur',NULL),(37,'007 Le monde ne suffit pas',NULL),(38,'Little Big Adventure',NULL),(39,'Tekken 3',NULL),(40,'Goldeneye',NULL),(41,'Zelda Ocarina Of Time',NULL),(42,'Zelda Majora\'s Mask',NULL),(43,'1080° Snowboarding',NULL),(44,'World Cup 98',NULL),(45,'Mario 64',NULL),(46,'Mario Golf',NULL),(47,'Mario Tennis',NULL),(48,'Mario Kart 64',NULL),(49,'Yoshi\'s Story',NULL),(50,'Sonic Adventure',NULL),(51,'V-Rally 2  Expert Edition',NULL),(52,'Confict Zone',NULL),(53,'Speed Devils',NULL),(54,'Evolution the world of sacred device',NULL),(56,'Trick Style',NULL),(58,'Resident Evil Code Veronica',NULL),(59,'F355 Challenge',NULL),(60,'Vigilant 8 2nd Offense',NULL),(61,'Tekken Tag',NULL),(62,'Crash Bandicoot: La vengeance de Cortex',NULL),(64,'Pro Evolution Soccer 2',NULL),(68,'Silent Hill 4',NULL),(69,'Le monde des bleus 2002',NULL),(70,'Silent Hill 3',NULL),(71,'Silent Hill 2',NULL),(72,'Tekken 5',NULL),(73,'Silent Hill Origins',NULL),(74,'Resident Evil 0',NULL),(75,'Zelda WindWaker',NULL),(76,'Mario Party 5',NULL),(78,'NBA Courtside 2002',NULL),(79,'Eternal Darkness',NULL),(80,'Super Smash Bros Melee',NULL),(81,'Mario Kart Double Dash',NULL),(82,'Zelda Twilight Princess',NULL),(83,'Donkey Konga 2',NULL),(84,'Resident Evil Umbrella Chronicles',NULL),(85,'Mario Kart Wii',NULL),(86,'Les lapins crétins: retour vers le passé',NULL),(87,'Super Mario Bros Wii',NULL),(88,'Resident Evil The Dark Side Chronicle',NULL),(89,'Disaster day of crisis',NULL),(90,'The Dead Rising',NULL),(91,'Wii Sports',NULL),(92,'Super Smash Bros Brawl',NULL),(93,'Epic Mickey',NULL),(94,'Donkey Kong Country Returns',NULL),(95,'Band Hero',NULL),(96,'Titanic: An Adventure Out Of Time',NULL),(97,'Démonts et Manants',NULL),(98,'Silent Hunter II',NULL),(99,'Starcraft Brood War',NULL),(100,'IL2 Sturmovik',NULL),(101,'The FullThrottle',NULL),(102,'Gabriel Knight II: The Beast Whithin',NULL),(104,'Medal Of Honor l\'Offensive',NULL),(105,'Pirates',NULL),(106,'The Settlers II - Tenth anniversary edition',NULL),(107,'Age of Empires II',NULL),(108,'Age Of Empires II The Conquerors',NULL),(110,'Commandos II',NULL),(111,'Pro Evolution Soccer 6',NULL),(112,'Iznogoud',NULL),(113,'Rise Of Nations Throne & Patriots',NULL),(114,'Commandos: Derrière les lignes ennemies',NULL),(115,'Commandos: Le sens du devoir',NULL),(116,'SPQR',NULL),(117,'Frankeinstein The Eyes of the Monster',NULL),(119,'Carmageddon',NULL),(120,'Carmageddon 2',NULL),(121,'Starcraft',NULL),(122,'Tomb Raider II',NULL),(123,'Marine Malice et le Mystère des graines d\'algues',NULL),(124,'Worms Fort Etat de Siège',NULL),(125,'F22 Lighting II',NULL),(126,'Combat Flight Simulator',NULL),(127,'Red Baron 3D',NULL),(128,'Rise of Nations  ',NULL),(129,'Medal Of Honor Spearhead',NULL),(130,'Little Big Adventure 2',NULL),(132,'Aces over Europe',NULL),(133,'Aces of the Pacific',NULL),(134,'Red Baron',NULL),(135,'A-10 Tank Killer',NULL),(136,'The aviation pionneers',NULL),(137,'Command Aces of the Deep',NULL),(138,'A10-II Silent Thunder',NULL),(139,'Monkey Island IV',NULL),(140,'Monkey Island III',NULL),(141,'Egypte 1',NULL),(142,'Power Chess',NULL),(143,'Worms Armagueddon',NULL),(144,'Le bouclier de Quetzacoatl (Broken sword II)',NULL),(145,'Les chevaliers de Baphomet (Broken Sword 1)',NULL),(146,'688 Sumarine',NULL),(147,'Aces High',NULL),(148,'Destroyer Simulation',NULL),(149,'Warbird 2',NULL),(150,'Caesar 2',NULL),(152,'Dreadnough',NULL),(153,'Half Life',NULL),(154,'Holiday Island',NULL),(155,'Liverpool FC',NULL),(156,'Monkey Island II',NULL),(157,'Project IGI',NULL),(158,'Transport Tycoon Deluxe',NULL),(159,'Tomb Raider IV',NULL),(160,'The Last Express',NULL),(161,'Age Of Empires III',NULL),(162,'Age Of Empires III Warchiefs',NULL),(163,'Age Of Empires III Asian Dynasties',NULL),(164,'Grim Fandango',NULL),(165,'Phantasmagoria',NULL),(166,'Hitman',NULL),(167,'Metal Rage',NULL),(168,'Virtua Tennis 3',NULL),(169,'Sega Rally 2',NULL),(170,'Dust A tale in the wired west',NULL),(171,'Football Manager 96/97',NULL),(172,'Le trésor du San Diego',NULL),(174,'Versailles II',NULL),(175,'The X Files',NULL),(176,'Titanic un voyage interactif',NULL),(177,'Crazy Taxi',NULL),(178,'Tout le bridge aujourd\'hui',NULL),(179,'Dracula 2',NULL),(180,'Constructor',NULL),(181,'Morrowind',NULL),(182,'Splinter Cell',NULL),(183,'Virtua Tennis',NULL),(184,'Mafia 2',NULL),(185,'Silent Hunter IV',NULL),(186,'Black And White 2',NULL),(187,'Medal Of Honor Allied Assault',NULL),(188,'Versailles',NULL),(189,'Un voisin d\'enfer',NULL),(190,'Alice Madness Returns',NULL),(191,'Silent Hunter III',NULL),(192,'Star Wars Knights Of The Old Republic',NULL),(193,'Syberia',NULL),(194,'Virtual Pool',NULL),(195,'Descent',NULL),(196,'Need For Speed V',NULL),(197,'Need For Speed III',NULL),(198,'Les Visiteurs: la relique de Sainte Rolande',NULL),(199,'Les cochons de guerre',NULL),(200,'Age of Empires Gold',NULL),(201,'Discworld',NULL),(202,'Discworld 2',NULL),(203,'Lemmings Revolution',NULL),(204,'Screamer 4x4 Rally',NULL),(205,'Theme Hospital',NULL),(206,'Woodruff',NULL),(207,'Mafia',NULL),(208,'Fighting Steel',NULL),(209,'Oblivion',NULL),(210,'Tribunal (ext. Morrowind)',NULL),(211,'Syberia 2',NULL),(213,'Shivers',NULL),(214,'Desperados I : Wanted Dead or Alive',NULL),(215,'Runaway',NULL),(217,'Trine 2',NULL),(218,'Trine 1',NULL),(219,'Beetle Crazy Cup',NULL),(220,'Tomb Raider III',NULL),(222,'Football Manager 98/99',NULL),(223,'Simcity 2000',NULL),(224,'Conker\'s Bad Fur Day',NULL),(225,'Myst',NULL),(229,'Runaway 2',NULL),(230,'Runaway 3 ',NULL),(231,'Syberia 3',NULL),(232,'Daria',NULL),(233,'Football Manager 2005',NULL),(234,'Gobliiins',NULL),(236,'Midtown Madness',NULL),(237,'Midtown Madness 2',NULL),(239,'Ecstatica 2',NULL),(240,'Pandemonium',NULL),(241,'Pandemonium 2',NULL),(243,'L\'Amerzone',NULL),(245,'Leisure Suit Larry I: in the Land of the Lounge Lizards',NULL),(246,'The dig',NULL),(247,'Simon the sorcerer',NULL),(248,'Yesterday Origins',NULL),(249,'The day of the tentacle',NULL),(250,'Nibiru : age of secrets',NULL),(251,'Gabriel Knight I: Sins of The Father',NULL),(252,'Super Mario Land 2',NULL),(253,'Bloodmoon (Extension Morrowind)',NULL),(255,'Black and White',NULL),(256,'Phantasmagoria : obsessions fatales',NULL),(257,'Alone in the dark',NULL),(258,'Combat Flight Simulator 2',NULL),(259,'Dino Crisis 2',NULL),(260,'Thimbleweed Park',NULL),(261,'Sam and Max',NULL),(262,'Indiana Jones and the fate of Atlantis',NULL),(263,'Paradise',NULL),(264,'Ace Ventura',NULL),(265,'Kursk',NULL),(267,'Gabriel Knight III: Blood of the Sacred, Blood of the Damned',NULL),(269,'Back to the Future: The Game',NULL),(270,'Atlantis',NULL),(271,'Dino Crisis',NULL),(273,'Chicago 1930',NULL),(274,'Warcraft Adventures',NULL),(275,'Fallout',NULL),(276,'Dune',NULL),(277,'Loom',NULL),(279,'Another World',NULL),(281,'Gobliins 2: The Prince Buffoon',NULL),(282,'Goblins Quest 3',NULL),(283,'Indiana Jones and the last crusade',NULL),(284,'Blade Runner',NULL),(285,'Warcraft II',NULL),(286,'Pompei',NULL),(287,'Tomb Raider V',NULL),(288,'Myst II : Riven',NULL),(289,'Myst III - Exile',NULL),(290,'Dracula',NULL),(291,'Leisure Suit Larry II: Goes Looking for Love (in Several Wrong Places)',NULL),(292,'Leisure Suit Larry III: Passionate Patti in Pursuit of the Pulsating Pectorals',NULL),(293,'Leisure Suit Larry V: Passionate Patti Does a Little Undercover Work',NULL),(294,'Leisure Suit Larry VI: Shape Up or Slip Out!',NULL),(295,'Leisure Suit Larry VII: Love for Sail!',NULL),(296,'Leisure Suit Larry: Magna Cum Laude',NULL),(297,'Leisure Suit Larry: Box Office Bust',NULL),(298,'Leisure Suit Larry: Reloaded',NULL),(299,'Leisure Suit Larry: Wet Dreams Don\'t Dry',NULL),(300,'Pro Evolution Soccer',NULL),(301,'Vigilante 8',NULL),(304,'Rayman contre les lapins encore + crétins',NULL),(305,'Jack in the Dark',NULL),(307,'Alone in the Dark 3 ',NULL),(308,'Alone in the Dark: The New Nightmare',NULL),(309,'Les Visiteurs : le jeu',NULL),(310,'Dark Earth',NULL),(311,'Star Wars racer',NULL),(312,'Desperados II: Western Commandos : La Revanche de Cooper',NULL),(313,'Desperados: Helldorado',NULL),(314,'Desperados III',NULL),(315,'Max Payne',NULL),(316,'Panzer General II',NULL),(319,'Myst IV: Revelation',NULL),(320,'Uru: ages beyond Myst',NULL),(321,'Rule the waves II',NULL),(322,'Caesar 3',NULL),(323,'Pharaon',NULL),(325,'Broken Sword 3: The Sleeping Dragon',NULL),(326,'Broken Sword 4: The Angel of Death',NULL),(327,'Broken Sword 5: The Serpent\'s Curse',NULL),(328,'Tales of Monkey Island: chapter 1',NULL),(329,'Tales of Monkey Island: chapter 2 The siege of spinner cay',NULL),(330,'Tales of Monkey Island: chapter 3: lair of the leviathan',NULL),(331,'Tales of Monkey Island: chapter 4: the trial and execution of Guybrush Threepwood',NULL),(332,'Tales of Monkey Island: chapter 5: rise of the pirate god',NULL),(333,'Jack and Daxter',NULL),(334,'Lost Horizon',NULL),(335,'Paris 1313 le disparu de notre dame',NULL),(337,'Egypte II',NULL),(338,'Chine intrigue dans la cité interdite',NULL),(339,'American McGee\'s Alice',NULL),(340,'WWII Online',NULL),(341,'Rayman 2: The Great Escape',NULL),(342,'Star Wars: Episode I Battle for Naboo',NULL),(343,'Space Station Silicon Valley',NULL),(344,'Indiana Jones et la Machine Infernale',NULL),(345,'Parasite Eve',NULL),(346,'The Legend of Zelda: A Link to the Past',NULL),(347,'Soccer',NULL),(348,'Fifa 2000',NULL),(349,'Sonic R',NULL),(350,'Luigi\'s Mansion',NULL),(351,'Atlantis II',NULL),(352,'Fifa 11',NULL),(354,'Alone in the Dark 2: One eyed Jack\'s Revenge',NULL),(355,'Pilot Wings',NULL),(356,'Beetle Adventures Racing',NULL),(357,'Yoshi\'s Island',NULL),(358,'Donkey Kong Country',NULL),(359,'Donkey Kong 64',NULL),(360,'The Settlers II',NULL),(361,'Discworld noir',NULL),(362,'Beavis and Butt-Head in Virtual Stupidity',NULL),(363,'Deus ex',NULL),(364,'Rayman 3: Hoodlum Havoc',NULL),(366,'Swat 2',NULL),(367,'Quest for Glory: Shadows of Darkness',NULL),(368,'Simcity 3000',NULL),(369,'Faust',NULL),(370,'Pilgrim',NULL),(371,'Aztec',NULL),(372,'Cossacks',NULL),(373,'Anno 1602',NULL),(374,'Panzer Commander',NULL),(375,'Croc: legend of the gobbos',NULL),(376,'Fifa 99',NULL),(377,'Destruction Derby',NULL),(378,'Soviet Strike',NULL),(379,'Tonic Trouble',NULL),(380,'Flight Simulator 2000',NULL);
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
  `type` varchar(255) NOT NULL,
  `notes` text,
  PRIMARY KEY (`trade_id`),
  KEY `copy_id` (`copy_id`),
  CONSTRAINT `trades_ibfk_1` FOREIGN KEY (`copy_id`) REFERENCES `copies` (`copy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trades`
--

LOCK TABLES `trades` WRITE;
/*!40000 ALTER TABLE `trades` DISABLE KEYS */;
INSERT INTO `trades` VALUES (90,1,2022,2,4,'Loan-out',''),(91,1,2022,4,8,'Loan-out-return','');
/*!40000 ALTER TABLE `trades` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (90,348,1,2022,2,4,'Loan-out',''),(91,348,1,2022,4,8,'Loan-out-return',''),(92,349,2,2022,2,4,'Loan-out',''),(93,349,2,2022,2,5,'Loan-in',''),(106,340,NULL,2022,3,4,'Sold',NULL);
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
INSERT INTO `users` VALUES (1,'foo@bar.com','802cee6fdb8f3964700a7d789bd034cee6e5dba100f2c3df1fcb2b9afdc97b2b','kK0pXVUq',1,'Eric','tokentest123');
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
) ENGINE=InnoDB AUTO_INCREMENT=350 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `versions`
--

LOCK TABLES `versions` WRITE;
/*!40000 ALTER TABLE `versions` DISABLE KEYS */;
INSERT INTO `versions` VALUES (1,7,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,'top en coop !!!',0,0,0,0,0),(2,7,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(3,7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(4,7,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(5,7,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(6,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(7,7,7,0,0,0,0,0,0,0,0,0,0,0,1,1996,1,1,0,NULL,0,0,0,0,0),(8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(10,8,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(11,8,11,0,1,0,0,0,0,0,0,0,0,0,1,1998,8,1,0,NULL,0,0,0,0,0),(12,8,13,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(13,8,14,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(14,8,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(15,8,16,0,0,0,0,0,0,0,0,0,0,0,1,1998,7,1,0,NULL,0,0,0,0,0),(16,2,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(17,2,18,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(18,2,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(19,2,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(20,2,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(21,2,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(22,2,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(23,2,24,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,8,0),(24,2,25,0,0,0,0,0,0,0,0,0,1,1,1,1999,4,0,0,NULL,0,1,0,0,0),(25,2,26,0,0,0,0,0,0,0,0,0,1,1,1,2001,3,0,0,NULL,0,0,0,0,0),(26,2,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(27,2,28,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(28,2,29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(29,2,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(30,2,31,0,0,0,0,0,0,0,0,0,0,0,1,2000,3,0,0,NULL,0,0,0,0,0),(31,2,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(32,2,33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(33,2,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(34,2,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(35,2,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(36,2,37,0,0,0,0,0,0,0,0,0,1,0,1,2000,5,0,0,NULL,0,0,0,0,0),(37,2,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(38,2,39,0,0,0,0,0,0,0,0,0,0,0,1,2000,6,1,0,NULL,0,0,0,0,0),(39,4,40,0,0,1,0,0,0,0,0,0,0,0,1,1997,2,1,0,NULL,0,0,0,0,0),(40,4,41,0,0,0,0,0,0,0,0,0,0,1,1,1999,2,0,0,NULL,0,1,0,0,0),(41,4,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(42,4,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(43,4,44,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(44,4,45,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(45,4,46,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(46,4,47,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(47,4,48,0,0,1,0,0,0,0,0,0,0,1,1,1998,6,1,0,NULL,0,1,0,0,0),(48,4,49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(49,9,50,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(50,9,51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(51,9,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(52,9,53,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(53,9,54,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(54,9,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(55,9,58,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(56,9,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(57,9,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(58,3,61,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(59,3,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(60,3,64,0,0,1,0,0,0,0,0,0,0,0,1,2002,4,1,0,NULL,0,0,0,0,0),(61,3,68,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(62,3,69,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(63,3,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(64,3,71,0,0,0,0,0,0,0,0,0,1,1,1,2001,4,0,0,NULL,0,1,0,0,0),(65,3,72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(66,3,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(67,5,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(68,5,75,0,0,0,0,0,0,0,0,0,0,0,1,2004,5,0,0,NULL,0,0,0,0,0),(69,5,76,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(70,5,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(71,5,78,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(72,5,79,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,3,0),(73,5,80,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(74,5,81,0,0,1,0,0,0,0,0,0,0,0,1,2003,3,1,0,NULL,0,0,0,0,0),(75,5,82,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(76,5,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(77,6,84,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(78,6,85,0,0,1,0,0,0,0,0,0,0,0,1,2008,1,1,0,NULL,0,0,0,0,0),(79,6,86,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(80,6,87,0,1,1,0,0,0,0,0,0,0,1,1,2022,5,0,0,NULL,0,0,0,0,0),(81,6,88,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(82,6,89,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(83,6,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(84,6,91,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(85,6,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(86,6,93,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(87,6,94,0,1,1,0,0,0,0,0,0,0,0,1,2021,5,0,0,NULL,0,0,0,0,0),(88,6,95,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(89,1,96,0,0,0,0,0,1,0,0,0,0,1,1,1998,1,1,0,NULL,0,1,0,10,0),(90,1,97,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(91,1,98,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(92,1,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(93,1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(94,1,101,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(95,1,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(96,1,104,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(97,1,105,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(98,1,106,0,0,0,1,0,0,0,0,0,0,0,1,2007,2,0,0,NULL,1,0,0,0,0),(99,1,107,0,0,0,0,0,0,0,0,0,0,1,1,1999,6,1,0,NULL,0,0,0,0,0),(100,1,108,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(101,1,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(102,1,110,0,0,0,0,1,1,0,0,0,0,1,1,2003,2,1,0,NULL,0,1,0,0,0),(103,1,111,0,0,0,1,1,0,0,0,0,0,1,1,2006,1,0,0,NULL,0,0,0,0,0),(104,1,112,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(105,1,113,0,0,0,1,1,0,0,0,0,0,1,1,2004,1,1,0,NULL,0,0,0,0,0),(106,1,114,0,0,0,0,1,0,0,0,0,0,0,1,1999,8,0,1,NULL,0,0,0,0,0),(107,1,115,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(108,1,116,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(109,1,117,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(110,1,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(111,1,119,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(112,1,120,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(113,1,121,0,0,0,0,0,0,0,0,0,0,0,1,1999,3,1,0,NULL,0,0,0,0,0),(114,1,122,0,0,0,0,0,1,0,0,0,0,0,1,1998,10,0,0,NULL,0,0,0,6,0),(115,1,123,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(116,1,124,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(117,1,125,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(118,1,126,0,0,0,1,0,0,0,0,0,0,1,1,2001,2,1,0,NULL,0,0,0,0,0),(119,1,127,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(120,1,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(121,1,129,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(122,1,130,0,0,0,0,0,0,0,0,0,1,1,1,1997,1,0,0,NULL,0,1,0,0,0),(123,1,132,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(124,1,133,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(125,1,134,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(126,1,135,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(127,1,136,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(128,1,137,0,0,0,0,0,0,0,0,0,0,0,1,1999,1,1,0,NULL,0,1,0,0,0),(129,1,138,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(130,1,139,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(131,1,140,0,0,0,0,0,0,0,0,0,0,1,1,2001,1,1,0,NULL,0,1,0,0,0),(132,1,141,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(133,1,142,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(134,1,143,0,0,0,0,1,0,0,0,0,0,1,1,2001,8,1,0,NULL,0,0,0,0,0),(135,1,144,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(136,1,145,0,0,0,0,0,0,0,0,0,0,1,1,2001,6,0,0,NULL,0,0,0,0,0),(137,1,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(138,1,147,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(139,1,148,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(140,1,149,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(141,1,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(142,1,152,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(143,1,153,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(144,1,154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(145,1,155,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(146,1,156,0,0,0,0,0,0,0,0,0,0,0,1,2001,5,0,0,NULL,0,0,0,0,0),(147,1,157,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(148,1,158,0,0,0,1,0,0,0,0,0,0,1,1,1998,3,1,0,NULL,0,1,0,0,0),(149,1,159,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(150,1,160,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(151,1,161,0,0,0,0,0,0,1,0,0,0,1,1,2005,3,0,0,NULL,0,0,0,0,0),(152,1,162,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(153,1,163,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(154,1,164,0,0,0,0,0,0,0,0,0,0,0,1,2004,4,0,0,NULL,0,0,0,0,0),(155,1,165,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(156,1,166,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(157,1,167,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(158,1,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(159,1,169,0,1,0,0,0,0,0,0,0,0,0,1,2002,6,1,0,NULL,0,0,0,0,0),(160,1,170,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(161,1,171,0,0,0,0,0,0,0,0,0,0,0,1,1998,2,1,0,NULL,0,0,0,0,0),(162,1,172,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(163,1,174,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,NULL,1,0,0,0,0),(164,1,175,0,0,0,0,0,0,0,0,0,0,1,1,2000,1,0,0,NULL,1,0,0,0,0),(165,1,176,0,0,0,0,0,0,0,0,0,0,0,1,1996,2,0,0,NULL,0,0,0,0,0),(166,1,177,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(167,1,178,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(168,1,179,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(169,1,180,0,0,0,0,0,1,0,0,0,0,0,1,2001,7,0,0,NULL,1,0,0,13,0),(170,1,181,0,0,0,1,0,0,0,0,0,0,0,1,2002,1,0,0,NULL,0,1,0,0,0),(171,1,182,0,0,0,0,0,0,0,0,0,0,0,1,2010,1,0,0,NULL,0,0,0,0,0),(172,1,183,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(173,1,184,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(174,1,185,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(175,1,186,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(176,1,187,0,0,0,0,1,0,0,0,0,0,0,1,2002,3,1,0,NULL,0,0,0,0,0),(177,1,188,0,0,0,0,0,0,0,0,0,0,0,1,1999,7,0,0,NULL,1,0,0,0,0),(178,1,189,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(179,1,190,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(180,1,191,0,0,0,1,1,0,0,0,0,0,1,1,2005,1,1,0,NULL,0,1,0,0,0),(181,1,192,0,0,0,0,0,0,0,0,0,0,0,1,2005,2,1,0,NULL,0,0,0,0,0),(182,1,193,0,0,0,0,0,0,0,0,0,0,1,1,2004,2,0,0,NULL,0,0,0,0,0),(183,1,194,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(184,1,195,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(185,1,196,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(186,1,197,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(187,1,198,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(188,1,199,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(189,1,200,0,0,0,0,0,0,0,0,0,0,1,1,1998,5,1,0,NULL,0,0,0,0,0),(190,1,201,0,0,0,0,0,0,0,0,0,0,0,1,2012,1,0,0,NULL,0,0,0,0,0),(191,1,202,0,0,0,0,0,0,0,0,0,0,0,1,2022,3,0,0,NULL,0,0,0,0,0),(192,1,203,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(193,1,204,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(194,1,205,0,0,0,1,0,0,0,0,0,0,1,1,1998,4,1,0,NULL,0,0,0,0,0),(195,1,206,0,0,0,0,0,0,0,0,0,0,0,1,1998,8,0,0,NULL,1,0,0,0,0),(196,1,207,0,1,0,0,0,0,0,0,0,0,1,1,2003,1,1,0,NULL,0,0,0,0,0),(197,1,208,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,NULL,0,0,0,0,0),(198,1,209,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(199,1,210,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(200,1,211,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(201,1,213,0,0,0,0,0,0,0,0,0,0,0,1,2022,1,0,0,NULL,0,1,0,0,0),(202,1,214,0,0,0,0,0,1,0,0,0,0,0,1,2007,1,0,0,NULL,0,0,0,0,0),(203,1,215,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(204,1,217,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(205,1,218,0,0,0,0,0,0,0,0,0,0,0,1,2009,1,0,0,NULL,0,0,0,0,0),(206,1,219,0,1,1,0,0,0,0,0,0,0,0,1,2000,4,1,0,NULL,0,0,0,0,0),(207,1,220,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,99,0),(208,1,222,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,NULL,0,0,0,0,0),(209,1,223,0,0,0,1,0,0,0,0,0,0,1,1,1997,3,1,0,NULL,0,0,0,0,0),(210,4,224,0,0,0,0,0,0,0,0,0,0,1,1,2020,2,0,0,NULL,0,0,0,0,0),(211,1,225,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,12,0),(212,1,229,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(213,1,230,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(214,1,231,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(215,1,232,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(216,1,233,0,0,0,0,0,0,0,0,0,0,0,0,2005,4,0,0,NULL,0,0,0,0,0),(217,1,234,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(218,1,236,0,0,0,0,0,0,0,0,0,0,0,1,2000,2,1,0,NULL,0,0,0,0,0),(219,1,237,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(220,1,16,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(221,1,239,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(222,1,240,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(223,1,241,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(224,1,243,0,0,0,0,0,0,0,0,0,0,0,1,2022,2,0,0,NULL,0,0,0,0,0),(225,1,245,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(226,1,246,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(227,1,247,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(228,1,248,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(229,1,249,0,0,0,0,0,0,0,0,0,0,0,1,2004,3,0,0,NULL,0,0,0,0,0),(230,1,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(231,1,251,0,0,0,0,0,0,0,0,0,1,0,1,2018,1,0,0,NULL,0,1,0,0,0),(232,10,252,0,0,0,0,0,0,1,0,0,0,1,1,1993,1,1,0,NULL,0,0,0,0,0),(233,1,253,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(234,1,255,0,0,0,0,0,1,0,0,0,0,0,1,2002,5,0,0,NULL,0,0,0,9,0),(235,1,256,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(236,1,257,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(237,1,258,0,0,0,1,0,0,0,0,0,0,1,1,2002,5,1,0,NULL,0,0,0,0,0),(238,2,259,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(239,1,260,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(240,1,261,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(241,1,262,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(242,1,263,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(243,1,264,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(244,1,265,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(245,1,267,0,0,0,0,0,0,0,0,0,1,0,1,2020,3,0,0,NULL,0,0,0,0,0),(246,1,269,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(247,1,270,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(248,2,271,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(249,1,273,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(250,1,274,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(251,1,275,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(252,1,276,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(253,1,277,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(254,1,279,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(255,1,281,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(256,1,282,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(257,1,283,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(258,1,284,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(259,1,285,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(260,1,286,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(261,2,287,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(262,1,288,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(263,1,289,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(264,1,290,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(265,1,291,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(266,1,292,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(267,1,293,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(268,1,294,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(269,1,295,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(270,1,296,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(271,1,297,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(272,1,298,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(273,1,299,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(274,3,300,0,0,0,0,0,0,0,0,0,0,0,1,2002,2,0,0,NULL,0,0,0,0,0),(275,4,301,0,0,0,0,0,0,0,0,0,0,0,1,1999,5,0,0,NULL,0,0,0,0,0),(276,1,29,0,0,0,0,0,0,0,0,0,0,0,1,1997,4,1,0,NULL,0,0,0,0,0),(277,4,27,0,0,0,0,0,0,0,0,0,0,0,1,1997,4,0,0,NULL,0,0,0,0,0),(278,6,304,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(279,1,305,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(280,1,307,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(281,9,308,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,8,0),(282,1,309,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(283,1,310,0,0,0,0,0,0,0,0,0,0,0,1,2021,1,0,0,NULL,0,0,0,0,0),(284,1,311,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(285,1,312,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(286,1,313,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(287,1,314,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(288,1,315,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(289,1,316,0,0,0,1,1,0,0,0,0,0,1,1,2020,1,1,0,NULL,0,0,0,0,0),(290,1,319,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(291,1,320,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(292,1,321,0,0,0,1,0,0,0,0,0,0,1,1,2019,1,1,0,NULL,0,0,0,0,0),(293,1,322,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(294,1,323,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(295,1,325,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(296,1,326,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(297,1,327,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(298,1,328,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(299,1,329,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(300,1,330,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(301,1,331,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(302,1,332,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(303,3,333,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(304,1,334,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(305,1,335,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(306,1,287,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(307,1,337,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(308,1,338,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(309,1,339,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(310,1,340,0,1,0,0,0,0,0,0,0,0,1,1,2006,2,0,0,NULL,0,0,0,0,0),(311,4,341,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(312,4,342,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(313,4,343,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(314,1,344,0,0,0,0,0,0,0,0,0,0,0,1,2021,3,0,0,NULL,0,0,0,0,0),(315,2,345,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(316,11,346,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(317,10,347,0,0,0,0,0,0,0,0,0,0,0,1,1996,3,1,0,NULL,0,0,0,0,0),(318,1,348,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,NULL,0,0,0,0,0),(319,1,349,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(320,5,350,0,0,0,0,0,0,0,0,0,0,0,1,2021,2,0,0,NULL,0,0,0,0,0),(321,1,351,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(322,1,352,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(323,2,240,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,7,0),(324,2,354,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(325,4,355,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(326,4,356,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(327,11,357,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(328,11,358,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,11,0),(329,4,359,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(330,1,360,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(331,1,361,0,0,0,0,0,0,0,0,0,0,0,1,2022,4,0,0,NULL,0,0,0,0,0),(332,1,362,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(333,1,363,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(334,3,364,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(335,1,366,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(336,1,367,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(337,1,368,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(338,1,369,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(339,1,370,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(340,1,371,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(341,1,372,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(342,1,373,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,0,0),(343,1,374,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(344,2,375,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(345,1,376,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(346,8,377,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,4,0),(347,8,378,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,1,0,0,5,0),(348,1,379,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0),(349,1,380,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,NULL,0,0,0,0,0);
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

-- Dump completed on 2023-05-11 21:28:59
