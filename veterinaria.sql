-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: veterinaria
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
-- Table structure for table `historia`
--

DROP TABLE IF EXISTS `historia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `propietario` varchar(255) DEFAULT NULL,
  `cedula` varchar(15) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `medico_responsable` varchar(255) DEFAULT NULL,
  `fecha_creacion` date DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `nombre_paciente` varchar(255) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `especie` varchar(255) DEFAULT NULL,
  `raza` varchar(255) DEFAULT NULL,
  `sexo` varchar(10) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `vacuna_1` varchar(255) DEFAULT NULL,
  `fecha_vacuna_1` date DEFAULT NULL,
  `vacuna_2` varchar(255) DEFAULT NULL,
  `fecha_vacuna_2` date DEFAULT NULL,
  `vacuna_3` varchar(255) DEFAULT NULL,
  `fecha_vacuna_3` date DEFAULT NULL,
  `vacuna_4` varchar(255) DEFAULT NULL,
  `fecha_vacuna_4` date DEFAULT NULL,
  `vacuna_5` varchar(255) DEFAULT NULL,
  `fecha_vacuna_5` date DEFAULT NULL,
  `fecha_ultima_desparasitacion` date DEFAULT NULL,
  `motivo_consulta` text,
  `sintomatologia` text,
  `tratamiento` text,
  `diagnostico_diferencial` text,
  `examenes_complementarios` text,
  `diagnostico_definitivo` text,
  `tratamiento_final` text,
  `medicamento_1` varchar(255) NOT NULL,
  `posologia_1` varchar(255) NOT NULL,
  `medicamento_2` varchar(255) NOT NULL,
  `posologia_2` varchar(255) NOT NULL,
  `medicamento_3` varchar(255) NOT NULL,
  `posologia_3` varchar(255) NOT NULL,
  `medicamento_4` varchar(255) NOT NULL,
  `posologia_4` varchar(255) NOT NULL,
  `medicamento_5` varchar(255) NOT NULL,
  `posologia_5` varchar(255) NOT NULL,
  `proxima_cita` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historia`
--

LOCK TABLES `historia` WRITE;
/*!40000 ALTER TABLE `historia` DISABLE KEYS */;
/*!40000 ALTER TABLE `historia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historia_derma`
--

DROP TABLE IF EXISTS `historia_derma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historia_derma` (
  `id` int NOT NULL AUTO_INCREMENT,
  `propietario_d` varchar(255) DEFAULT NULL,
  `cedula_d` varchar(15) NOT NULL,
  `direccion_d` varchar(255) NOT NULL,
  `medico_responsable_d` varchar(255) DEFAULT NULL,
  `fecha_creacion_d` date DEFAULT NULL,
  `telefono_d` varchar(15) DEFAULT NULL,
  `nombre_paciente_d` varchar(255) NOT NULL,
  `fecha_nacimiento_d` date DEFAULT NULL,
  `especie_d` varchar(255) DEFAULT NULL,
  `raza_d` varchar(255) DEFAULT NULL,
  `sexo_d` varchar(10) DEFAULT NULL,
  `color_d` varchar(50) DEFAULT NULL,
  `vacuna_1_d` varchar(255) DEFAULT NULL,
  `fecha_vacuna_1_d` date DEFAULT NULL,
  `vacuna_2_d` varchar(255) DEFAULT NULL,
  `fecha_vacuna_2_d` date DEFAULT NULL,
  `vacuna_3_d` varchar(255) DEFAULT NULL,
  `fecha_vacuna_3_d` date DEFAULT NULL,
  `vacuna_4_d` varchar(255) DEFAULT NULL,
  `fecha_vacuna_4_d` date DEFAULT NULL,
  `vacuna_5_d` varchar(255) DEFAULT NULL,
  `fecha_vacuna_5_d` date DEFAULT NULL,
  `fecha_ultima_desparasitacion_d` date DEFAULT NULL,
  `motivo_consulta_d` text,
  `sintomatologia_d` text,
  `tratamiento_d` text,
  `diagnostico_diferencial_d` text,
  `otras_mascotas_d` varchar(255) DEFAULT NULL,
  `nin_casa_d` varchar(255) DEFAULT NULL,
  `familia_problema_d` varchar(255) DEFAULT NULL,
  `tipo_comida_d` text,
  `golosinas_d` varchar(255) DEFAULT NULL,
  `caida_pelo_d` varchar(255) DEFAULT NULL,
  `se_rasca_d` varchar(255) DEFAULT NULL,
  `ambiente_d` varchar(255) DEFAULT NULL,
  `pasa_sol_d` varchar(255) DEFAULT NULL,
  `pasa_tierra_d` varchar(255) DEFAULT NULL,
  `defecacion_d` varchar(255) DEFAULT NULL,
  `parte_enrojecida_d` varchar(255) DEFAULT NULL,
  `fecha_ectoparasitos_d` date DEFAULT NULL,
  `descrip_ectoparasitos_d` text,
  `duchas_casa_d` varchar(255) DEFAULT NULL,
  `alergia_comida_d` varchar(255) DEFAULT NULL,
  `rasp_cutaneo_d` text,
  `tricograma_d` text,
  `lampara_wood_d` text,
  `reflejo_otopodal_d` text,
  `biopsia_d` text,
  `citologia_d` text,
  `antibiograma_d` text,
  `diagnostico_definitivo_d` text,
  `tratamiento_final_d` text,
  `medicamento_1_d` varchar(255) DEFAULT NULL,
  `posologia_medicamento_1_d` text,
  `medicamento_2_d` varchar(255) DEFAULT NULL,
  `posologia_medicamento_2_d` text,
  `medicamento_3_d` varchar(255) DEFAULT NULL,
  `posologia_medicamento_3_d` text,
  `medicamento_4_d` varchar(255) DEFAULT NULL,
  `posologia_medicamento_4_d` text,
  `medicamento_5_d` varchar(255) DEFAULT NULL,
  `posologia_medicamento_5_d` text,
  `proxima_cita_d` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historia_derma`
--

LOCK TABLES `historia_derma` WRITE;
/*!40000 ALTER TABLE `historia_derma` DISABLE KEYS */;
/*!40000 ALTER TABLE `historia_derma` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-18 11:22:45
