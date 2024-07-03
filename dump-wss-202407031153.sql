-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: wss
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `actividad`
--

DROP TABLE IF EXISTS `actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividad` (
  `id_actividad` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(35) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `riesgo` varchar(30) NOT NULL,
  `medida_control` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_actividad`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividad`
--

LOCK TABLES `actividad` WRITE;
/*!40000 ALTER TABLE `actividad` DISABLE KEYS */;
INSERT INTO `actividad` VALUES (1,'Cortes','Medio','Guantes Anticorte'),(2,'Masado de muestras','TMERT','Adoptar buenas posturas'),(3,'Lixiviaxión','Caída mismo nivel','Mantener área ordena y limpia'),(4,'Digestión acida','Inhalación gases toxicos','Uso de respirador y careta'),(5,'Lavado de material','Quemadura con plancha','Utilizar EPP'),(6,'Lectura de muestras por absorcion','Exposición UV','Uso de protector, mantener distancia'),(7,'Test','Caida mismo nivel','Mantener área ordenada y limpia');
/*!40000 ALTER TABLE `actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `art`
--

DROP TABLE IF EXISTS `art`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `art` (
  `id_ART` int NOT NULL AUTO_INCREMENT,
  `trabajo_simultaneo` tinyint(1) NOT NULL,
  `id_actividad` int NOT NULL,
  `estado_trabajador` tinyint(1) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_termino` time NOT NULL,
  PRIMARY KEY (`id_ART`),
  KEY `id_actividad` (`id_actividad`),
  CONSTRAINT `art_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `actividad` (`id_actividad`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `art`
--

LOCK TABLES `art` WRITE;
/*!40000 ALTER TABLE `art` DISABLE KEYS */;
INSERT INTO `art` VALUES (1,1,1,1,'00:00:00','00:00:00'),(2,0,2,1,'00:00:00','00:00:00'),(3,0,1,0,'00:00:00','00:00:00'),(4,1,4,1,'00:00:00','00:00:00'),(5,1,3,0,'00:00:00','00:00:00'),(6,1,1,1,'22:26:21','00:18:00'),(7,1,1,1,'22:29:19','00:18:00'),(8,1,1,1,'22:29:24','00:18:00'),(9,1,1,1,'22:29:50','00:18:00'),(10,1,1,1,'22:30:26','00:18:00'),(11,1,1,1,'22:30:26','00:18:00'),(12,1,1,1,'22:31:14','00:18:00'),(13,1,1,1,'22:31:14','00:18:00'),(14,1,1,1,'22:34:40','24:18:00'),(15,1,1,1,'22:41:01','24:18:00'),(16,1,1,1,'22:46:57','18:27:00');
/*!40000 ALTER TABLE `art` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleado` (
  `rut` char(9) NOT NULL,
  `nombre_completo` varchar(30) NOT NULL,
  `correo` varchar(30) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion_residencia` varchar(30) NOT NULL,
  `cargo` varchar(20) NOT NULL,
  `contraseña` varchar(20) NOT NULL,
  PRIMARY KEY (`rut`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES ('123456789','Alvaro Vergara','elperroloco@gmail.com','222222222','antofa','Supervisor','Alvaricoque'),('187697653','Carolina Ramirez','Carolina123@gmail.com','989976554','dos','Supervisor','carolina123'),('208971234','Vladimir Heriquez ','Vladimir@gmail.com','978653454','tres','Químico analista','vladimmir1234'),('218679323','Margarita cordera','margarita@gmail.com','73378556','uno','Tec, Quimico','maar123'),('224750987','Karen Herrera','Karen12@gmail.com','941281473','cero','Auxliar Lavado','Karen123'),('236980472','Checo Perez','Chequito@gmail.com','+579524256','Le mans','Supervisor','Samuel123');
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incorpora`
--

DROP TABLE IF EXISTS `incorpora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incorpora` (
  `id_art` int NOT NULL,
  `id_pregunta` int NOT NULL,
  `respuesta` tinyint(1) NOT NULL,
  KEY `incorpora_FK` (`id_art`),
  KEY `incorpora_FK_1` (`id_pregunta`),
  CONSTRAINT `incorpora_FK` FOREIGN KEY (`id_art`) REFERENCES `art` (`id_ART`),
  CONSTRAINT `incorpora_FK_1` FOREIGN KEY (`id_pregunta`) REFERENCES `pregunta` (`id_pregunta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incorpora`
--

LOCK TABLES `incorpora` WRITE;
/*!40000 ALTER TABLE `incorpora` DISABLE KEYS */;
/*!40000 ALTER TABLE `incorpora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posee`
--

DROP TABLE IF EXISTS `posee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posee` (
  `id_actividad` int NOT NULL,
  `id_riesgoCritico` int NOT NULL,
  KEY `id_actividad` (`id_actividad`),
  KEY `id_riesgoCritico` (`id_riesgoCritico`),
  CONSTRAINT `posee_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `actividad` (`id_actividad`),
  CONSTRAINT `posee_ibfk_2` FOREIGN KEY (`id_riesgoCritico`) REFERENCES `riesgocritico` (`id_riesgoCritico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posee`
--

LOCK TABLES `posee` WRITE;
/*!40000 ALTER TABLE `posee` DISABLE KEYS */;
INSERT INTO `posee` VALUES (1,1),(2,2),(3,4);
/*!40000 ALTER TABLE `posee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pregunta`
--

DROP TABLE IF EXISTS `pregunta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pregunta` (
  `id_pregunta` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  `cargo` varchar(45) NOT NULL,
  PRIMARY KEY (`id_pregunta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pregunta`
--

LOCK TABLES `pregunta` WRITE;
/*!40000 ALTER TABLE `pregunta` DISABLE KEYS */;
/*!40000 ALTER TABLE `pregunta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `realiza`
--

DROP TABLE IF EXISTS `realiza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `realiza` (
  `rut` char(9) NOT NULL,
  `id_ART` int NOT NULL,
  `fecha` date NOT NULL,
  KEY `rut` (`rut`),
  KEY `id_ART` (`id_ART`),
  CONSTRAINT `realiza_ibfk_1` FOREIGN KEY (`rut`) REFERENCES `empleado` (`rut`),
  CONSTRAINT `realiza_ibfk_2` FOREIGN KEY (`id_ART`) REFERENCES `art` (`id_ART`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `realiza`
--

LOCK TABLES `realiza` WRITE;
/*!40000 ALTER TABLE `realiza` DISABLE KEYS */;
INSERT INTO `realiza` VALUES ('187697653',1,'2024-07-15'),('208971234',15,'2024-06-26'),('208971234',16,'2024-06-26');
/*!40000 ALTER TABLE `realiza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `riesgocritico`
--

DROP TABLE IF EXISTS `riesgocritico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `riesgocritico` (
  `id_riesgoCritico` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `pregunta` int NOT NULL,
  `respuesta_correcta` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_riesgoCritico`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `riesgocritico`
--

LOCK TABLES `riesgocritico` WRITE;
/*!40000 ALTER TABLE `riesgocritico` DISABLE KEYS */;
INSERT INTO `riesgocritico` VALUES (1,'Test 1 ',1,1),(2,'Test 1',1,1),(3,'Test 3',1,0),(4,'Test 4',1,1);
/*!40000 ALTER TABLE `riesgocritico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `ver_arts`
--

DROP TABLE IF EXISTS `ver_arts`;
/*!50001 DROP VIEW IF EXISTS `ver_arts`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ver_arts` AS SELECT 
 1 AS `rut`,
 1 AS `nombre_completo`,
 1 AS `fecha`,
 1 AS `hora_inicio`,
 1 AS `hora_termino`,
 1 AS `trabajo_simultaneo`,
 1 AS `nombre`,
 1 AS `estado_trabajador`,
 1 AS `cargo`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'wss'
--

--
-- Final view structure for view `ver_arts`
--

/*!50001 DROP VIEW IF EXISTS `ver_arts`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ver_arts` AS select `e`.`rut` AS `rut`,`e`.`nombre_completo` AS `nombre_completo`,`r`.`fecha` AS `fecha`,`a`.`hora_inicio` AS `hora_inicio`,`a`.`hora_termino` AS `hora_termino`,`a`.`trabajo_simultaneo` AS `trabajo_simultaneo`,`ac`.`nombre` AS `nombre`,`a`.`estado_trabajador` AS `estado_trabajador`,`e`.`cargo` AS `cargo` from (((`art` `a` left join `realiza` `r` on((`r`.`id_ART` = `a`.`id_ART`))) left join `empleado` `e` on((`e`.`rut` = `r`.`rut`))) left join `actividad` `ac` on((`a`.`id_actividad` = `ac`.`id_actividad`))) where (`e`.`rut` = `r`.`rut`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-03 11:53:37
