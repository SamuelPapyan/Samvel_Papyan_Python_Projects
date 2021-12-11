-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy_db
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

drop database if exists `pharmacy_db`;
create database `pharmacy_db`;
use `pharmacy_db`;


--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Pain Medicine'),(2,'Soar Throat Medicine'),(3,'Heartburn Medicine');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drug_contents`
--

DROP TABLE IF EXISTS `drug_contents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug_contents` (
  `id` int NOT NULL AUTO_INCREMENT,
  `drug_id` int NOT NULL,
  `content_item` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug_contents`
--

LOCK TABLES `drug_contents` WRITE;
/*!40000 ALTER TABLE `drug_contents` DISABLE KEYS */;
INSERT INTO `drug_contents` VALUES (1,1,'Ibuprofen'),(2,2,'Dichrorobenzyl Alcohol'),(3,2,'Amylmetacresol'),(4,3,'Sodium Alginate'),(5,3,'Sodium Bicarbonate'),(6,3,'Calcium Carbonate'),(13,7,'cont1'),(14,7,'cont2'),(15,7,'cont3'),(16,8,'Content 1'),(17,8,'Content 2'),(18,8,'Content 3'),(24,11,'dsfa'),(25,11,'dsaf'),(26,11,'sadf');
/*!40000 ALTER TABLE `drug_contents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drug_in_pharmacy`
--

DROP TABLE IF EXISTS `drug_in_pharmacy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug_in_pharmacy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `drug_id` int NOT NULL,
  `pharmacy_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug_in_pharmacy`
--

LOCK TABLES `drug_in_pharmacy` WRITE;
/*!40000 ALTER TABLE `drug_in_pharmacy` DISABLE KEYS */;
INSERT INTO `drug_in_pharmacy` VALUES (1,1,1),(2,2,1),(3,1,2),(4,2,2),(5,3,2),(6,2,3),(7,3,3),(15,1,8),(16,7,8),(19,7,10),(20,8,10);
/*!40000 ALTER TABLE `drug_in_pharmacy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drug_side_effects`
--

DROP TABLE IF EXISTS `drug_side_effects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug_side_effects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `drug_id` int NOT NULL,
  `side_effect_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug_side_effects`
--

LOCK TABLES `drug_side_effects` WRITE;
/*!40000 ALTER TABLE `drug_side_effects` DISABLE KEYS */;
INSERT INTO `drug_side_effects` VALUES (1,1,'Constipation'),(2,1,'Dizziness'),(3,1,'Nervousness'),(4,2,'Hiccups'),(5,2,'Heartburn'),(11,7,'side1'),(12,7,'side2'),(13,7,'side3'),(14,8,'Side 1'),(15,8,'Side 2'),(16,8,'Side 3'),(19,11,'dsaf'),(20,11,'asef'),(21,11,'sadf');
/*!40000 ALTER TABLE `drug_side_effects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drugs`
--

DROP TABLE IF EXISTS `drugs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drugs` (
  `drug_id` int NOT NULL AUTO_INCREMENT,
  `sales_method` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `price` int NOT NULL,
  `dose` float NOT NULL,
  `description` varchar(50) NOT NULL,
  `manufacturer_id` int NOT NULL,
  `supplier_id` int NOT NULL,
  `drug_type` varchar(50) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `expiration_date` date NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`drug_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drugs`
--

LOCK TABLES `drugs` WRITE;
/*!40000 ALTER TABLE `drugs` DISABLE KEYS */;
INSERT INTO `drugs` VALUES (1,'ByRecipe','Nurofen',12000,400,'Pain Medicine',1,1,'Pill','Bayer','2022-05-22',1),(2,'FreeSale','Strepsils',15000,350,'Sore Throat Medicine',2,2,'Pill','BAYER','2022-06-17',2),(3,'ByRecipe','Geviscon',16000,350,'Heartburn Medicine',3,3,'Liquid','BAYER','2022-07-23',3),(7,'FreeSale','My Drug 1',12000,2.3,'This is my description 1',5,5,'Pill','My Brand','2012-02-02',6),(8,'FreeSale','My Drug 2',1100,2.5,'This is my custom drug 2',5,5,'Pill','My Custom Brand','2016-03-03',6),(11,'FreeSale','My Drug 5',12300,2.6,'fdsafsa',3,3,'Liquid','fdsaf','2022-04-12',3);
/*!40000 ALTER TABLE `drugs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `manufacturer_id` int NOT NULL AUTO_INCREMENT,
  `contact_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  PRIMARY KEY (`manufacturer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
INSERT INTO `manufacturers` VALUES (1,'Artyom Markosyan','Abovyan str 12','+374 10 765912','Armenia'),(2,'Karen Davtyan','Komitas ave 14','+374 12 950123','Armenia'),(3,'David Karapetyan','Sayat-Nova ave 12','+374 14 981254','Armenia');
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pharmacies`
--

DROP TABLE IF EXISTS `pharmacies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pharmacies` (
  `pharmacy_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `sales_method` varchar(50) NOT NULL,
  `pharmacy_network_id` int NOT NULL,
  PRIMARY KEY (`pharmacy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharmacies`
--

LOCK TABLES `pharmacies` WRITE;
/*!40000 ALTER TABLE `pharmacies` DISABLE KEYS */;
INSERT INTO `pharmacies` VALUES (1,'AlfaPharm','Komitas Ave. 46','ByRecipe',1),(2,'Natali Pharm','Komitas Ave. 1','FreeSale',2),(3,'36 6','Abovyan Str. 36','ByRecipe',3),(8,'My Phrmacy 1','Komitas Ave. 37/4','FreeSale',5),(10,'My Pharm 3.0','Sargisyan Ave. 14','ByRecipe',5);
/*!40000 ALTER TABLE `pharmacies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pharmacy_networks`
--

DROP TABLE IF EXISTS `pharmacy_networks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pharmacy_networks` (
  `pharmacy_network_id` int NOT NULL AUTO_INCREMENT,
  `website_link` varchar(100) NOT NULL,
  PRIMARY KEY (`pharmacy_network_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharmacy_networks`
--

LOCK TABLES `pharmacy_networks` WRITE;
/*!40000 ALTER TABLE `pharmacy_networks` DISABLE KEYS */;
INSERT INTO `pharmacy_networks` VALUES (1,'alfapharm.am'),(2,'natali-pharm.am'),(3,'36-6.com'),(6,'www.my_own_pharm.com');
/*!40000 ALTER TABLE `pharmacy_networks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `supplier_id` int NOT NULL AUTO_INCREMENT,
  `contact_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Daniel Sargsyan','Baghramyan ave 14','+374 97 921466','Armenia'),(2,'Rafi Hovhannisyan','Azatutyan ave 29','+374 91 861234','Armenia'),(3,'Narek Sargsyan','Tumanyan str 13','+374 97 861423','Armenia');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-11  0:20:40
