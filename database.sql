-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: tweeterdb
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `address_id` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `street_name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `street_number` int DEFAULT NULL,
  `country` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `region` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `zipcode` int DEFAULT NULL,
  PRIMARY KEY (`address_id`),
  UNIQUE KEY `address_id_UNIQUE` (`address_id`),
  KEY `addresses_ibfk_1` (`zipcode`),
  CONSTRAINT `addresses_ibfk_1` FOREIGN KEY (`zipcode`) REFERENCES `zipcodes` (`zipcode`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` VALUES ('091910c2-0f68-4576-8cdd-14ec1ec38f29','alanis',23,'alanis','alanis',244),('1027fe73-5dee-4496-a138-a32a67f8c452','BuiÄi 84 A',NULL,'Croatia','istra',52000),('33131494-1068-45ca-aa26-c93a8c9b7e38','wldkwl',223,'lwdkwl','lwkdlw',12),('67d0a82b-7160-43a2-80e1-fd5863b911aa','Buići 84 A',123,'Croatia','alanis',9000),('bc070186-407c-4d47-a550-fe4b5e134c2d','alanis',12,'alanis','alanis',123),('d11f7998-85a6-4727-95ae-0ce3f197516c','alanis',2,'alanis','alanis',233),('d483c927-b324-446f-a4cd-d8a95b28a5d0','martin',123,'potato','istraofcourse',1234);
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follows`
--

DROP TABLE IF EXISTS `follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `follows` (
  `user_email_initiator` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_email_receiver` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  UNIQUE KEY `user_email_initiator` (`user_email_initiator`,`user_email_receiver`),
  KEY `user_email_receiver` (`user_email_receiver`),
  CONSTRAINT `follows_ibfk_5` FOREIGN KEY (`user_email_receiver`) REFERENCES `users` (`user_email`),
  CONSTRAINT `follows_ibfk_6` FOREIGN KEY (`user_email_initiator`) REFERENCES `users` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follows`
--

LOCK TABLES `follows` WRITE;
/*!40000 ALTER TABLE `follows` DISABLE KEYS */;
INSERT INTO `follows` VALUES ('alanismirko@gmail.com','a@a.com'),('alanismirko@gmail.com','alanis@alanis.com'),('a@a.com','alanismirko@gmail.com');
/*!40000 ALTER TABLE `follows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessions`
--

DROP TABLE IF EXISTS `sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessions` (
  `session_id` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `session_user_email` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `session_created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`session_id`),
  UNIQUE KEY `session_id_UNIQUE` (`session_id`),
  KEY `session_user_email` (`session_user_email`),
  CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`session_user_email`) REFERENCES `users` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status` (
  `status_id` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `status_type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`status_id`),
  UNIQUE KEY `status_id_UNIQUE` (`status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tweets` (
  `tweet_id` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `tweet_description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `tweet_title` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `tweet_created_at` int unsigned NOT NULL,
  `tweet_updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tweet_user_email` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `tweet_image_id` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `tweet_likes` int DEFAULT NULL,
  `tweet_dislikes` int DEFAULT NULL,
  PRIMARY KEY (`tweet_id`),
  UNIQUE KEY `tweet_id_UNIQUE` (`tweet_id`),
  KEY `tweet_user_email` (`tweet_user_email`),
  FULLTEXT KEY `tweet_title` (`tweet_title`,`tweet_description`),
  FULLTEXT KEY `tweet_title_2` (`tweet_title`,`tweet_description`),
  FULLTEXT KEY `tweet_title_3` (`tweet_title`),
  FULLTEXT KEY `tweet_description` (`tweet_description`),
  CONSTRAINT `tweets_ibfk_2` FOREIGN KEY (`tweet_user_email`) REFERENCES `users` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES ('2ece57ba-ef89-4859-8670-1e57a1718d6f','alanis','alanis',1649861669,'2022-04-13 14:54:29','a@a.com','6940e604-12a4-4736-a70c-dfd7bbfe40d6.png',NULL,NULL),('6b9a764b-de7a-4ce9-ab3a-e190d6119615','fkjefke','fjejfkwe',1647934133,'2022-03-22 07:28:53','alanis@alanis.com',NULL,NULL,NULL),('8a263602-6aec-41de-8b9c-dcf909d2e363','jkdwkdwkkjkjkk','kjkjkkjkjlkklk',1647933377,'2022-04-01 13:50:12','alanismirko@gmail.com',NULL,NULL,NULL),('a748bdb7-faee-46c6-94ed-38eed4cfe527','nhn','gtggb',1649859312,'2022-04-13 14:15:12','alanismirko@gmail.com','bf23e8d4-3888-45fa-9c59-8c286b89fd15.png',NULL,NULL),('baa5930d-4fe0-449b-a641-dce57fdb431c','b','ala',1650452560,'2022-04-20 11:02:40','alanismirko@gmail.com','nothing',NULL,NULL),('c3c59dc0-29fd-46c0-a590-cc228b16b913','eevwev','sceewv',1650528936,'2022-04-21 08:15:36','alanismirko@gmail.com','No image added',NULL,NULL);
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets_liked`
--

DROP TABLE IF EXISTS `tweets_liked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tweets_liked` (
  `tweet_id` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_email` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  UNIQUE KEY `tweet_id` (`tweet_id`,`user_email`),
  KEY `tweets_liked_ibfk_2` (`user_email`),
  CONSTRAINT `tweets_liked_ibfk_1` FOREIGN KEY (`tweet_id`) REFERENCES `tweets` (`tweet_id`),
  CONSTRAINT `tweets_liked_ibfk_2` FOREIGN KEY (`user_email`) REFERENCES `users` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets_liked`
--

LOCK TABLES `tweets_liked` WRITE;
/*!40000 ALTER TABLE `tweets_liked` DISABLE KEYS */;
INSERT INTO `tweets_liked` VALUES ('2ece57ba-ef89-4859-8670-1e57a1718d6f','alanismirko@gmail.com'),('6b9a764b-de7a-4ce9-ab3a-e190d6119615','alanismirko@gmail.com');
/*!40000 ALTER TABLE `tweets_liked` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_first_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_last_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_created_at` int NOT NULL,
  `user_updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_address_id` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `user_image_id` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`user_id`,`user_email`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `user_email_UNIQUE` (`user_email`),
  KEY `users_address_id` (`user_address_id`),
  FULLTEXT KEY `user_email` (`user_email`),
  FULLTEXT KEY `user_email_2` (`user_email`),
  FULLTEXT KEY `user_email_3` (`user_email`),
  FULLTEXT KEY `user_email_4` (`user_email`),
  CONSTRAINT `users_address_id` FOREIGN KEY (`user_address_id`) REFERENCES `addresses` (`address_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('1','admin','admin','admin@gmail.com','admin',1649843593,'2022-04-19 19:34:00',NULL,NULL),('12f151f9-fbf0-483b-9a07-7359470ddef2','Opg','Mirko','a@a.com','$2b$12$XJXrLZFLFtASM3bq2NF5TO2h/BYBk8mkC0caSb.Z5g7pITT7ck8i.',1649843593,'2022-04-13 09:53:13','d11f7998-85a6-4727-95ae-0ce3f197516c','a0451a8a-8a5d-43ad-b1c6-792e39b434cb.png'),('17c82ae2-21ab-4ac1-9d38-943f77122ad5','kjkdj','k','wld','$2b$12$e5pB4zMJZr3f29bhGMT3yuvqoLs9YyZdmEMIqRugsc2BED47/tICe',1650394534,'2022-04-19 18:55:35','33131494-1068-45ca-aa26-c93a8c9b7e38','fceb7649-aa15-4406-8bb0-9dfbc7c15514.png'),('1fc9c82e-3244-42c1-b85d-57654062','alanis','mirko','alanis@alanis.com','alanis123',0,'0000-00-00 00:00:00',NULL,NULL),('2cd9d9d6-6c26-4dd2-8b2f-098a7e256b8a','Alanis','Mirko','agnezamirko1@gmail.com','$2b$12$W/riahfUeXn.tHXSRLXYDukChTo40zdEqoioPAINyxwgIfFQ3L0FO',1649171747,'2022-04-05 15:15:47','1027fe73-5dee-4496-a138-a32a67f8c452',NULL),('4b6bfb03-c717-4a67-a612-b355258cbd8d','alvaro','mato','alvaro@gmail.com','mirko11',1647978020,'2022-03-22 19:40:20',NULL,NULL),('84548199-033b-4704-92ef-fa99be1b1dea','Alanis','Mirko','alanis@gmail.com','alanis',1647977755,'2022-03-22 19:35:55',NULL,NULL),('898a46ab-349f-459f-ad6c-86bcf0e36e54','Martin','Hotka','martin@gmail.com','$2b$12$4jUKCm6ZXbxTMfGREv3qI.jlxpNfQmvIS4B.LHGQdFmiS6RnbxLgO',1649190597,'2022-04-05 20:29:57','d483c927-b324-446f-a4cd-d8a95b28a5d0',NULL),('a0b827ae-b700-4724-96de-635352f5ac05','Alanis','Mirko','alan1200@stud.kea.dk','alanis',1647977710,'2022-03-22 19:35:10',NULL,NULL),('cd243c3a-500b-475f-8fac-376b50e9e204','A','Mirko','f@f.com','$2b$12$fam/u7avxXZBx.HVb6iAdu8ZkNhX3OwhoMsDrt4Iq2DYKLoqqzqBC',1650439088,'2022-04-20 07:18:08','67d0a82b-7160-43a2-80e1-fd5863b911aa','d0ab5149-5671-4eb8-95e6-06e0ed535248.png'),('cffc87ed-7555-4f51-9860-cc6e6401','Alanis','Mirko','alanismirko@gmail.com','alanis',1647350403,'0000-00-00 00:00:00',NULL,NULL),('eea6c6fe-9c0f-4e98-8feb-1847f0058999','Opg','Mirko','b@b.com','$2b$12$FzFuC3Ju4YxmAB9QL8xVmOfLbDKK1kmKAYmUqKvSqvAFWClLscwh6',1650391157,'2022-04-19 17:59:18','bc070186-407c-4d47-a550-fe4b5e134c2d','dccce5b4-ad14-46a8-93bd-1a85c6e39b69.png'),('f686e5e1-5454-4967-9ec7-a5bbb70522c6','Alanis','Mirko','gabrijelmirkoiscool@gmail.com','$2b$12$bZKEGyTQ.pB6k2InuLgi3uGdgtE6kWo2FkPjU.zM.wymW6NVs8sw2',1649169805,'2022-04-05 14:43:26',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zipcodes`
--

DROP TABLE IF EXISTS `zipcodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zipcodes` (
  `zipcode` int NOT NULL,
  `city` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`zipcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zipcodes`
--

LOCK TABLES `zipcodes` WRITE;
/*!40000 ALTER TABLE `zipcodes` DISABLE KEYS */;
INSERT INTO `zipcodes` VALUES (12,'ekel'),(123,'alanis'),(233,'alanis'),(244,'alanis'),(1234,'fritule'),(9000,'Pazin'),(52000,'Pazin');
/*!40000 ALTER TABLE `zipcodes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-24  9:12:53
