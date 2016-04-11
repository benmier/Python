-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: friendsdb2
-- ------------------------------------------------------
-- Server version	5.6.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `message_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (5,'123','2016-03-15 18:53:39','2016-03-15 18:53:39',18,15),(6,'test','2016-03-15 19:19:51','2016-03-15 19:19:51',18,13),(7,'12345','2016-03-15 19:20:04','2016-03-15 19:20:04',18,12),(8,'gwet','2016-03-15 19:20:17','2016-03-15 19:20:17',18,5),(9,'test','2016-03-15 19:20:31','2016-03-15 19:20:31',18,15),(10,'post','2016-03-15 19:21:53','2016-03-15 19:21:53',16,2),(11,'test','2016-03-15 19:21:57','2016-03-15 19:21:57',16,2),(12,'asd','2016-03-15 19:22:01','2016-03-15 19:22:01',16,1);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'test test test','2016-03-15 16:39:11','2016-03-15 16:39:11',16),(2,'test2 test2 test2','2016-03-15 16:39:40','2016-03-15 16:39:40',16),(3,'test3 test3 test3','2016-03-15 16:40:31','2016-03-15 16:40:31',17),(4,'test4 test4 test4','2016-03-15 16:40:31','2016-03-15 16:40:31',17),(5,'test5 test5 test5','2016-03-15 17:23:39','2016-03-15 17:23:39',18),(9,'asdasd','2016-03-15 17:35:03','2016-03-15 17:35:03',18),(10,'asdasd','2016-03-15 17:36:51','2016-03-15 17:36:51',18),(11,'asdasd','2016-03-15 17:37:21','2016-03-15 17:37:21',18),(12,'qwe','2016-03-15 17:40:05','2016-03-15 17:40:05',18),(13,'asd','2016-03-15 17:48:21','2016-03-15 17:48:21',18),(14,'qweqweqweqweq','2016-03-15 17:51:17','2016-03-15 17:51:17',18),(15,'qweqwe','2016-03-15 18:03:04','2016-03-15 18:03:04',18);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (16,'Benjamin','Mier','bencmier@gmail.com','$2b$12$R/eCy.9JFjCzzPzRpPt4EeBWo7pRHAHH7xUpjFydX5f6c773gvgxK','2016-03-15 16:36:37','2016-03-15 16:36:37'),(17,'Melissa','Villeneuve','mjeanvil@gmail.com','$2b$12$3ECRERcBIdQ7kLZ0yhuB/.78Uw1ASw/gpWIsnkQeLPZp2JCgnLx8y','2016-03-15 16:36:57','2016-03-15 16:36:57'),(18,'Benjamin','Mier','asd','$2b$12$NTRdPEGR4WmoILh1e0LGYOaI.2/Hp3pr43EkC5bSJ9S9manRoIrKe','2016-03-15 17:16:46','2016-03-15 17:16:46');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-15 19:22:57
