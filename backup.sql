-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: lion
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `nombre` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` VALUES ('Admin','elp4n4d3r0');
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agentes`
--

DROP TABLE IF EXISTS `agentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agentes` (
  `idAgente` int NOT NULL AUTO_INCREMENT,
  `Fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `NombresCompletos` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Password` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `NivelDeEstudios` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `NombreEscuela` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `EstadoDeSalud` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Enfermedades` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ConsumoSustancias` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `AntiguosEmpleos` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Edad` int DEFAULT NULL,
  `Celular1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Celular2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Correo1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Correo2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Direccion` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Observaciones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Activo` int DEFAULT NULL,
  `NombreContacto` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Hobbies` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idAgente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agentes`
--

LOCK TABLES `agentes` WRITE;
/*!40000 ALTER TABLE `agentes` DISABLE KEYS */;
INSERT INTO `agentes` VALUES (1,'2023-11-14 00:10:28','Ivan Hernandez','password1234','Prepa trunca','Esteban','Con la muñeca fracturada','Espero que ninguna','Se ve','Panadero',30,'?','?','?','?','Enrique Segobiano','?',1,'Ivan','?');
/*!40000 ALTER TABLE `agentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asesorias`
--

DROP TABLE IF EXISTS `asesorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asesorias` (
  `idAsesoria` int NOT NULL AUTO_INCREMENT,
  `Fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `NombreDelCliente` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Ocupacion` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Celular` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `TemaAsesoria` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `idAgente` int DEFAULT NULL,
  `NombreAgente` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Observaciones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idAsesoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asesorias`
--

LOCK TABLES `asesorias` WRITE;
/*!40000 ALTER TABLE `asesorias` DISABLE KEYS */;
/*!40000 ALTER TABLE `asesorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atenciones`
--

DROP TABLE IF EXISTS `atenciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atenciones` (
  `idAtencion` int NOT NULL AUTO_INCREMENT,
  `idCliente` int DEFAULT NULL,
  `ElaboradoPor` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Cargo` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Actividad` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `idNegocio` int DEFAULT NULL,
  `idOperacion` int DEFAULT NULL,
  `PropuestasYSoluciones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `DetallesRelevantes` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Proposito_objetivo` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Conclusiones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Activo` int DEFAULT NULL,
  PRIMARY KEY (`idAtencion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atenciones`
--

LOCK TABLES `atenciones` WRITE;
/*!40000 ALTER TABLE `atenciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `atenciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `idCliente` int NOT NULL AUTO_INCREMENT,
  `Fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `NombresCompletos` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `NombreNegocio` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Celular1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Celular2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Telefono1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Correo1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Correo2` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Ciudad` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Direccion` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Observaciones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `RFC` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Regimen` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `NSS` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `CP` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `OpinionDeCumplimiento` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `LicACargo` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emprendedores`
--

DROP TABLE IF EXISTS `emprendedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emprendedores` (
  `idClientes` int NOT NULL AUTO_INCREMENT,
  `Fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `idCliente` int DEFAULT NULL,
  `idAgente` int DEFAULT NULL,
  `idEstado` int DEFAULT NULL,
  `idServicio` int DEFAULT NULL,
  `CapitalInicial` int DEFAULT NULL,
  `Activo` int DEFAULT NULL,
  `NombreProyecto` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Pm` int DEFAULT NULL,
  `Pf` int DEFAULT NULL,
  `Regimen` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Direccion` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Giro` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Producto` int DEFAULT NULL,
  `Servicio` int DEFAULT NULL,
  `Marketing` int DEFAULT NULL,
  `Gestion` int DEFAULT NULL,
  `EquipoTrabajo` int DEFAULT NULL,
  `NumeroTrabajadores` int DEFAULT NULL,
  `InovacionTecnologica` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Observaciones` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idClientes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emprendedores`
--

LOCK TABLES `emprendedores` WRITE;
/*!40000 ALTER TABLE `emprendedores` DISABLE KEYS */;
/*!40000 ALTER TABLE `emprendedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados`
--

DROP TABLE IF EXISTS `estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados` (
  `idEstado` int NOT NULL AUTO_INCREMENT,
  `Estado` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idEstado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados`
--

LOCK TABLES `estados` WRITE;
/*!40000 ALTER TABLE `estados` DISABLE KEYS */;
/*!40000 ALTER TABLE `estados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operaciones`
--

DROP TABLE IF EXISTS `operaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operaciones` (
  `idOperacion` int NOT NULL AUTO_INCREMENT,
  `Operacion` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Campo1` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idOperacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operaciones`
--

LOCK TABLES `operaciones` WRITE;
/*!40000 ALTER TABLE `operaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `operaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regimen`
--

DROP TABLE IF EXISTS `regimen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regimen` (
  `idRegimen` int NOT NULL AUTO_INCREMENT,
  `Regimen` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idRegimen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regimen`
--

LOCK TABLES `regimen` WRITE;
/*!40000 ALTER TABLE `regimen` DISABLE KEYS */;
/*!40000 ALTER TABLE `regimen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `idServicios` int NOT NULL AUTO_INCREMENT,
  `Servicio` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`idServicios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-13 18:18:26
