CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (14,'Divergent','V',NULL,NULL),(15,'Divergent','Veronica Roth',NULL,NULL),(16,'The Vampire Chronicles','Joe Blow',NULL,NULL),(17,'The Life of Pie','Someone Cool',NULL,NULL),(18,'Divergent','Veronica Roth',NULL,NULL),(19,'Tuesdays with Morrie','Who Knows',NULL,NULL),(20,'The Greatest Salesman in the World','Jim Bob',NULL,NULL),(21,'Divergent','Veronica Roth',NULL,NULL),(22,'Divergent','Veronica Roth',NULL,NULL),(23,'Divergent','Veronica Roth',NULL,NULL),(24,'Divergent','Veronica Roth',NULL,NULL),(25,'Divergent','Veronica Roth',NULL,NULL);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `review` text,
  `rating` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `review_user_id` int(11) NOT NULL,
  `review_book_id` int(11) NOT NULL,
  PRIMARY KEY (`review_id`),
  KEY `fk_reviews_users_idx` (`review_user_id`),
  KEY `fk_reviews_books1_idx` (`review_book_id`),
  CONSTRAINT `fk_reviews_users` FOREIGN KEY (`review_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_books1` FOREIGN KEY (`review_book_id`) REFERENCES `books` (`book_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (12,'I like the book than the movie.',4,'2016-03-20 10:06:05','2016-03-20 10:06:05',6,15),(13,'Cool stuff, me love it long time',5,'2016-03-20 10:07:32','2016-03-20 10:07:32',6,16),(14,'Wow amazing books and stuff!',3,'2016-03-20 10:08:02','2016-03-20 10:08:02',6,17),(15,'This is a review!',2,'2016-03-20 10:10:05','2016-03-20 10:10:05',7,15),(16,'Drama and inspiration.',4,'2016-03-20 10:16:36','2016-03-20 10:16:36',8,19),(17,'Very inspiring. Gives a lot of wisdom an relationship with people and an achieving one\'s goals.',5,'2016-03-20 10:18:58','2016-03-20 10:18:58',9,20),(22,'I love the action!',4,'2016-03-20 10:46:58','2016-03-20 10:46:58',10,15);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `confirm` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (6,'Jessie Jamie','Jessie','jessiej@yahoo.com','$2b$12$UjX2Jhg2WgntRrFlA4IAQeVLfERN9OKjXySdBAQkFSQFaroLigHii',NULL,'2016-03-20 10:04:44','2016-03-20 10:04:44'),(7,'Shirley Woohoo','Shirley','s@w.com','$2b$12$NuhTZNr8gQRVVSRHR4FXcunKaxTXKgUSzb4Kk6oqpW79ZrDX4zlXe',NULL,'2016-03-20 10:09:43','2016-03-20 10:09:43'),(8,'Mike Motown','Mike','m@m.com','$2b$12$eONaG.zx9Ak.h5UdmUzmteYnngEqiJ..6fSV6mTg7KiOkqPMZGEaO',NULL,'2016-03-20 10:16:11','2016-03-20 10:16:11'),(9,'Jerry Johnson','Jerry','j@j.com','$2b$12$whz07cOyfazSOT.SFFwuvOLIjmwD7.LRKocAv9JHmaEeowWIfzfaa',NULL,'2016-03-20 10:17:46','2016-03-20 10:17:46'),(10,'David Dope','David','d@d.com','$2b$12$dyfTauWB82LhaNyzNWNuV.3LyjJsu/4DlAX9NhXZa.NUZ9YEn7eTS',NULL,'2016-03-20 10:19:52','2016-03-20 10:19:52');
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

-- Dump completed on 2016-03-20 10:49:58
