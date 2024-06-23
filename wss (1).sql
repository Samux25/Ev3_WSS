-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-06-2024 a las 01:37:08
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `wss`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `id_actividad` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `riesgo` varchar(30) NOT NULL,
  `medida_control` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `actividad`
--

INSERT INTO `actividad` (`id_actividad`, `nombre`, `riesgo`, `medida_control`) VALUES
(1, 'Cortes', 'Medio', 'Guantes Anticorte'),
(2, 'Masado de muestras', 'TMERT', 'Adoptar buenas posturas'),
(3, 'Lixiviaxión', 'Caída mismo nivel', 'Mantener área ordena y limpia'),
(4, 'Digestión acida', 'Inhalación gases toxicos', 'Uso de respirador y careta'),
(5, 'Lavado de material', 'Quemadura con plancha', 'Utilizar EPP'),
(6, 'Lectura de muestras por absorc', 'Exposición UV', 'Uso de protector, mantener dis');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art`
--

CREATE TABLE `art` (
  `id_ART` int(11) NOT NULL,
  `trabajo_simultaneo` tinyint(1) NOT NULL,
  `id_actividad` int(11) NOT NULL,
  `preguntas_trabajador` varchar(30) DEFAULT NULL,
  `estado_trabajador` tinyint(1) NOT NULL,
  `preguntas_supervisor` varchar(30) NOT NULL,
  `fecha` date NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_termino` char(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `art`
--

INSERT INTO `art` (`id_ART`, `trabajo_simultaneo`, `id_actividad`, `preguntas_trabajador`, `estado_trabajador`, `preguntas_supervisor`, `fecha`, `hora_inicio`, `hora_termino`) VALUES
(1, 1, 1, 'true true true', 1, 'true true true true', '2024-06-15', '15:03:03', '1800'),
(2, 0, 2, 'uno uno uno', 1, 'dos dos dos', '2024-08-02', '09:00:00', '2100'),
(3, 0, 1, 'tres tres', 0, 'cuatro cuatro', '2024-08-02', '14:30:00', '1830'),
(4, 1, 4, 'uno dos tres', 1, 'tres dos uno', '2024-05-23', '21:00:00', '0900'),
(5, 1, 3, 'uno dos dos', 0, 'tres uno uno', '2024-01-30', '09:00:00', '1830');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `rut` char(9) NOT NULL,
  `nombre_completo` varchar(30) NOT NULL,
  `correo` varchar(30) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion_residencia` varchar(30) NOT NULL,
  `cargo` varchar(20) NOT NULL,
  `contraseña` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`rut`, `nombre_completo`, `correo`, `telefono`, `direccion_residencia`, `cargo`, `contraseña`) VALUES
('187697653', 'Carolina Ramirez', 'Carolina123@gmail.com', '989976554', 'dos', 'Supervisor', 'carolina123'),
('208971234', 'Vladimir Heriquez ', 'Vladimir@gmail.com', '978653454', 'tres', 'Químico analista', 'vladimmir1234'),
('218679323', 'Margarita cordera', 'margarita@gmail.com', '73378556', 'uno', 'Tec, Quimico', 'maar123'),
('224750987', 'Karen Herrera', 'Karen12@gmail.com', '941281473', 'cero', 'Auxliar Lavado', 'Karen123'),
('236980472', 'Checo Perez', 'Chequito@gmail.com', '+579524256', 'Le mans', 'Supervisor', 'Samuel123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `posee`
--

CREATE TABLE `posee` (
  `id_actividad` int(11) NOT NULL,
  `id_riesgoCritico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `realiza`
--

CREATE TABLE `realiza` (
  `rut` char(9) NOT NULL,
  `id_ART` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `riesgocritico`
--

CREATE TABLE `riesgocritico` (
  `id_riesgoCritico` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `pregunta` int(5) NOT NULL,
  `respuesta_correcta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `riesgocritico`
--

INSERT INTO `riesgocritico` (`id_riesgoCritico`, `nombre`, `pregunta`, `respuesta_correcta`) VALUES
(1, 'Test 1 ', 1, 1),
(2, 'Test 1', 1, 1),
(3, 'Test 3', 1, 0),
(4, 'Test 4', 1, 1);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `supervisores`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `supervisores` (
`rut` char(9)
,`nombre_completo` varchar(30)
,`telefono` varchar(20)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `supervisores`
--
DROP TABLE IF EXISTS `supervisores`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `supervisores`  AS SELECT `empleado`.`rut` AS `rut`, `empleado`.`nombre_completo` AS `nombre_completo`, `empleado`.`telefono` AS `telefono` FROM `empleado` WHERE `empleado`.`cargo` = 'supervisor' ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`id_actividad`);

--
-- Indices de la tabla `art`
--
ALTER TABLE `art`
  ADD PRIMARY KEY (`id_ART`),
  ADD KEY `id_actividad` (`id_actividad`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`rut`);

--
-- Indices de la tabla `posee`
--
ALTER TABLE `posee`
  ADD KEY `id_actividad` (`id_actividad`),
  ADD KEY `id_riesgoCritico` (`id_riesgoCritico`);

--
-- Indices de la tabla `realiza`
--
ALTER TABLE `realiza`
  ADD KEY `rut` (`rut`),
  ADD KEY `id_ART` (`id_ART`);

--
-- Indices de la tabla `riesgocritico`
--
ALTER TABLE `riesgocritico`
  ADD PRIMARY KEY (`id_riesgoCritico`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividad`
--
ALTER TABLE `actividad`
  MODIFY `id_actividad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `art`
--
ALTER TABLE `art`
  MODIFY `id_ART` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `riesgocritico`
--
ALTER TABLE `riesgocritico`
  MODIFY `id_riesgoCritico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `art`
--
ALTER TABLE `art`
  ADD CONSTRAINT `art_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `actividad` (`id_actividad`);

--
-- Filtros para la tabla `posee`
--
ALTER TABLE `posee`
  ADD CONSTRAINT `posee_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `actividad` (`id_actividad`),
  ADD CONSTRAINT `posee_ibfk_2` FOREIGN KEY (`id_riesgoCritico`) REFERENCES `riesgocritico` (`id_riesgoCritico`);

--
-- Filtros para la tabla `realiza`
--
ALTER TABLE `realiza`
  ADD CONSTRAINT `realiza_ibfk_1` FOREIGN KEY (`rut`) REFERENCES `empleado` (`rut`),
  ADD CONSTRAINT `realiza_ibfk_2` FOREIGN KEY (`id_ART`) REFERENCES `art` (`id_ART`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
