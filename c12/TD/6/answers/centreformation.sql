/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.0.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: centreformation
-- ------------------------------------------------------
-- Server version	12.0.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `catalogue`
--

DROP TABLE IF EXISTS `catalogue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `catalogue` (
  `codeSpec` int(11) NOT NULL,
  `codeForm` int(11) NOT NULL,
  PRIMARY KEY (`codeSpec`,`codeForm`),
  KEY `codeForm` (`codeForm`),
  CONSTRAINT `catalogue_ibfk_1` FOREIGN KEY (`codeSpec`) REFERENCES `specialite` (`codeSpec`),
  CONSTRAINT `catalogue_ibfk_2` FOREIGN KEY (`codeForm`) REFERENCES `formation` (`codeForm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogue`
--

LOCK TABLES `catalogue` WRITE;
/*!40000 ALTER TABLE `catalogue` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `catalogue` VALUES
(101,11),
(101,12),
(103,13),
(104,13),
(104,14),
(101,15),
(102,15),
(104,16);
/*!40000 ALTER TABLE `catalogue` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `etudiant` (
  `numCINEtu` varchar(10) NOT NULL,
  `nomEtu` varchar(45) NOT NULL,
  `prenomEtu` varchar(45) NOT NULL,
  `dateNaissance` date NOT NULL,
  `adresseEtu` varchar(100) NOT NULL,
  `villeEtu` varchar(45) NOT NULL,
  `niveauScolaire` varchar(45) NOT NULL,
  PRIMARY KEY (`numCINEtu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etudiant`
--

LOCK TABLES `etudiant` WRITE;
/*!40000 ALTER TABLE `etudiant` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `etudiant` VALUES
('AB234567','Alami','Ahmad','1986-01-01','Rue du port, 13','Tanger','Bac'),
('C0987265','Toumi','Sanaa','1998-04-30','Place du peuple n 2','Tanger','Niveau Bac'),
('D2356903','Idrissi Alami','Mohammed','1996-05-05','Lotissement najah, rue n 12 immeuble 3','Rabat','Bac+ 4'),
('F9827363','El Khattabi','Fatima Zohra','1997-01-10','Immeuble iftikhar, n 13 ettakaddoum','Rabat','Bac + 2'),
('G5346789','Toumi','Aicha','2000-12-03','N12 immeuble Jaouhara','Casablanca','Master'),
('J3578902','Ben Omar','Abd Allah','1990-06-25','Villa Amina n12 bir rami','Kenitra','Phd'),
('Y1234987','Ouled thami','Ali','1979-12-04','La ville haute, rue chouhada n 6','Tanger','Bachelor');
/*!40000 ALTER TABLE `etudiant` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `formation`
--

DROP TABLE IF EXISTS `formation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `formation` (
  `codeForm` int(11) NOT NULL,
  `titreForm` varchar(45) NOT NULL,
  `dureeForm` double NOT NULL,
  `prixForm` double NOT NULL,
  `codeSess` int(11) DEFAULT NULL,
  PRIMARY KEY (`codeForm`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `formation`
--

LOCK TABLES `formation` WRITE;
/*!40000 ALTER TABLE `formation` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `formation` VALUES
(11,'Programming Java',12,3600,NULL),
(12,'Web Developpment',14,4200,NULL),
(13,'Anglais Technique',15,3700,NULL),
(14,'Communication',10,2500,NULL),
(15,'Inteligence Artificielle',20,6000,NULL),
(16,'Soft Skills',12,3000,NULL);
/*!40000 ALTER TABLE `formation` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `inscription`
--

DROP TABLE IF EXISTS `inscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscription` (
  `numCINEtu` varchar(10) NOT NULL,
  `codeSess` int(11) NOT NULL,
  `typeCours` varchar(45) NOT NULL,
  PRIMARY KEY (`numCINEtu`,`codeSess`),
  KEY `codeSess` (`codeSess`),
  CONSTRAINT `inscription_ibfk_1` FOREIGN KEY (`numCINEtu`) REFERENCES `etudiant` (`numCINEtu`),
  CONSTRAINT `inscription_ibfk_2` FOREIGN KEY (`codeSess`) REFERENCES `session` (`codeSess`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscription`
--

LOCK TABLES `inscription` WRITE;
/*!40000 ALTER TABLE `inscription` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `inscription` VALUES
('AB234567',1101,'Distanciel'),
('AB234567',1201,'Présentiel'),
('AB234567',1302,'Présentiel'),
('AB234567',1501,'Distanciel'),
('C0987265',1101,'Distanciel'),
('C0987265',1201,'Présentiel'),
('C0987265',1302,'Présentiel'),
('C0987265',1401,'Distanciel'),
('C0987265',1501,'Distanciel'),
('D2356903',1101,'Distanciel'),
('D2356903',1201,'Présentiel'),
('D2356903',1302,'Présentiel'),
('D2356903',1401,'Distanciel'),
('D2356903',1501,'Présentiel'),
('F9827363',1101,'Distanciel'),
('F9827363',1401,'Distanciel'),
('F9827363',1501,'Présentiel'),
('G5346789',1101,'Distanciel'),
('G5346789',1201,'Présentiel'),
('G5346789',1302,'Distanciel'),
('G5346789',1401,'Distanciel'),
('G5346789',1501,'Présentiel'),
('J3578902',1101,'Distanciel'),
('J3578902',1201,'Présentiel'),
('J3578902',1401,'Distanciel'),
('J3578902',1501,'Présentiel'),
('Y1234987',1101,'Distanciel'),
('Y1234987',1201,'Présentiel'),
('Y1234987',1302,'Présentiel'),
('Y1234987',1401,'Distanciel'),
('Y1234987',1501,'Présentiel');
/*!40000 ALTER TABLE `inscription` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `codeSess` int(11) NOT NULL,
  `nomSess` varchar(45) NOT NULL,
  `dateDebut` date NOT NULL,
  `dateFin` date NOT NULL,
  `codeForm` int(11) DEFAULT NULL,
  PRIMARY KEY (`codeSess`),
  KEY `codeForm` (`codeForm`),
  CONSTRAINT `session_ibfk_1` FOREIGN KEY (`codeForm`) REFERENCES `formation` (`codeForm`),
  CONSTRAINT `CHK_DATE` CHECK (`dateFin` > `dateDebut`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `session` VALUES
(1101,'Session1101','2022-01-02','2022-01-14',11),
(1102,'Session1102','2022-02-03','2022-02-15',11),
(1104,'Session1104','2022-10-15','2022-10-27',11),
(1201,'Session1201','2022-03-04','2022-03-18',12),
(1202,'Session1202','2022-04-05','2022-04-19',12),
(1203,'Session1203','2022-11-16','2022-11-30',12),
(1204,'Session1204','2022-12-17','2022-12-31',12),
(1301,'Session1301','2022-01-06','2022-01-21',13),
(1302,'Session1302','2022-05-07','2022-05-22',13),
(1303,'Session1303','2022-06-08','2022-06-23',13),
(1401,'Session1401','2022-09-01','2022-09-11',14),
(1402,'Session1402','2022-08-08','2022-08-18',14),
(1501,'Session1501','2022-11-11','2022-12-01',15),
(1502,'Session1502','2022-09-12','2022-10-02',15),
(1601,'Session1601','2022-09-13','2022-09-25',16),
(1602,'Session1602','2022-10-14','2022-10-26',16);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `specialite`
--

DROP TABLE IF EXISTS `specialite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `specialite` (
  `codeSpec` int(11) NOT NULL,
  `nomSpec` varchar(45) NOT NULL,
  `descSpec` varchar(45) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`codeSpec`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialite`
--

LOCK TABLES `specialite` WRITE;
/*!40000 ALTER TABLE `specialite` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `specialite` VALUES
(101,'GL','Genie logiciel et developpement',1),
(102,'Data','Data Engineering',1),
(103,'Langues','Anglais Français',1),
(104,'Communication','Communication',1),
(105,'Securite','Resaux et securite',0);
/*!40000 ALTER TABLE `specialite` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;
