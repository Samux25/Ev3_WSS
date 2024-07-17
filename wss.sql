-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-07-2024 a las 20:30:13
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

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
  `nombre` varchar(35) NOT NULL,
  `riesgo` varchar(30) NOT NULL,
  `medida_control` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `actividad`
--

INSERT INTO `actividad` (`id_actividad`, `nombre`, `riesgo`, `medida_control`) VALUES
(1, 'Lavado de material', 'Quemadura con plancha', 'Utilizar EPP'),
(2, 'Lecturas en equipo de A.A', 'Exposición UV', 'Uso de protector, mantener distancia'),
(3, 'Masado de muestras', 'TMERT', 'Adoptar buenas posturas'),
(4, 'Digestión acida de muestras', 'Inhalación gases toxicos', 'Uso de respirador y careta'),
(5, 'Lixiviaxión de muestras', 'Caída mismo nivel', 'Mantener área ordena y limpia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `art`
--

CREATE TABLE `art` (
  `id_ART` int(11) NOT NULL,
  `trabajo_simultaneo` tinyint(1) NOT NULL,
  `id_actividad` int(11) NOT NULL,
  `estado_trabajador` tinyint(1) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_termino` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `art`
--

INSERT INTO `art` (`id_ART`, `trabajo_simultaneo`, `id_actividad`, `estado_trabajador`, `hora_inicio`, `hora_termino`) VALUES
(1, 1, 1, 1, '00:00:00', '00:00:00'),
(2, 0, 2, 1, '00:00:00', '00:00:00'),
(3, 0, 1, 0, '00:00:00', '00:00:00'),
(4, 1, 4, 1, '00:00:00', '00:00:00'),
(5, 1, 3, 0, '00:00:00', '00:00:00'),
(6, 1, 1, 1, '22:26:21', '00:18:00'),
(7, 1, 1, 1, '22:29:19', '00:18:00'),
(8, 1, 1, 1, '22:29:24', '00:18:00'),
(9, 1, 1, 1, '22:29:50', '00:18:00'),
(10, 1, 1, 1, '22:30:26', '00:18:00'),
(11, 1, 1, 1, '22:30:26', '00:18:00'),
(12, 1, 1, 1, '22:31:14', '00:18:00'),
(13, 1, 1, 1, '22:31:14', '00:18:00'),
(14, 1, 1, 1, '22:34:40', '24:18:00'),
(15, 1, 1, 1, '22:41:01', '24:18:00'),
(16, 1, 1, 1, '22:46:57', '18:27:00'),
(18, 1, 3, 1, '23:29:21', '20:00:00'),
(19, 1, 3, 1, '23:30:47', '20:00:00'),
(20, 1, 3, 1, '01:37:11', '20:00:00'),
(21, 1, 3, 1, '22:08:28', '20:00:00');

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
  `especialidad` varchar(20) NOT NULL,
  `contraseña` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`rut`, `nombre_completo`, `correo`, `telefono`, `direccion_residencia`, `cargo`, `especialidad`, `contraseña`) VALUES
('123412344', 'Patricio la Estrella', 'patricioSexy@gmail.com', '956528381', 'en una piedra bajo del mar', 'Trabajador', 'Estrella de mar', 'qwerqwer'),
('123456789', 'Alvaro Vergara', 'elperroloco@gmail.com', '222222222', 'antofa', 'Supervisor', '', 'Alvaricoque'),
('187697653', 'Carolina Ramirez', 'Carolina123@gmail.com', '989976554', 'vasco de gama', 'Supervisor', '', 'carolina123'),
('208971234', 'Vladimir Heriquez ', 'Vladimir@gmail.com', '978653454', 'tres', 'Trabajador', 'Químico analista', 'vladimmir1234'),
('218679323', 'Margarita cordera', 'margarita@gmail.com', '73378556', 'uno', 'Trabajador', 'Tec, Quimico', 'maar123'),
('224750987', 'Karen Herrera', 'Karen12@gmail.com', '941281473', 'cero', 'Trabajador', 'Auxliar Lavado', 'Karen123'),
('236980472', 'Checo Perez', 'Chequito@gmail.com', '+579524256', 'Le mans', 'Supervisor', '', 'Samuel123'),
('76564345', 'no c', '12345@gmail.com', '98765432', 'no se', 'Trabajador', 'holaPrueba', 'asdfasdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `incorpora`
--

CREATE TABLE `incorpora` (
  `id_art` int(11) NOT NULL,
  `id_pregunta` int(11) NOT NULL,
  `respuesta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `posee`
--

CREATE TABLE `posee` (
  `id_actividad` int(11) NOT NULL,
  `id_riesgoCritico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `posee`
--

INSERT INTO `posee` (`id_actividad`, `id_riesgoCritico`) VALUES
(3, 6),
(5, 6),
(5, 7),
(4, 6),
(4, 7),
(1, 6),
(1, 7),
(2, 6),
(2, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pregunta`
--

CREATE TABLE `pregunta` (
  `id_pregunta` int(11) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `cargo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pregunta`
--

INSERT INTO `pregunta` (`id_pregunta`, `descripcion`, `cargo`) VALUES
(1, '¿El trabajo que asignaré cuenta con un estándar, procedimiento y/o instructivo?', 'Supervisor'),
(2, '¿El personal que asignaré para realizar el trabajo, cuenta con las capacitaciones, \r\ncompetencias, salud compatible y/o acreditaciones requeridas?', 'Supervisor'),
(3, '¿Durante la planificación del trabajo, me aseguro de solicitar los permisos para \ningresar a las áreas, intervenir equipos y/o interactuar con energías?', 'Supervisor'),
(4, 'Verifiqué que el personal cuenta con los elementos requeridos para realizar la \nsegregación y señalización del área de trabajo, según diseño?', 'Supervisor'),
(5, '¿El personal a mi cargo cuenta con sistema de comunicación de acuerdo al \r\nprotocolo de emergencia del área?', 'Supervisor'),
(6, '¿El personal que asignaré para realizar el trabajo, cuenta con los EPP definidos en \r\nel procedimiento de trabajo?', 'Supervisor'),
(7, '¿Conozco el estándar, procedimiento y/o instructivo del trabajo que ejecutaré?', 'Trabajador'),
(8, '¿Cuento con las competencias y salud compatible para ejecutar el trabajo?', 'Trabajador'),
(9, '¿Cuento con la autorización para ingresar al área a ejecutar el trabajo?', 'Trabajador'),
(10, '¿Segregué y señalicé el área de trabajo con los elementos según diseño?', 'Trabajador'),
(11, '¿Conozco el número de teléfono o frecuencia radial para dar aviso en caso de \r\nemergencia, según protocolo del área?', 'Trabajador'),
(12, '¿Uso los EPP definidos para el trabajo y se encuentran en buenas condiciones?', 'Trabajador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `realiza`
--

CREATE TABLE `realiza` (
  `rut` char(9) NOT NULL,
  `id_ART` int(11) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `realiza`
--

INSERT INTO `realiza` (`rut`, `id_ART`, `fecha`) VALUES
('187697653', 1, '2024-07-15'),
('208971234', 15, '2024-06-26'),
('208971234', 16, '2024-06-26'),
('123412344', 18, '2024-07-15'),
('123412344', 19, '2024-07-15'),
('123412344', 20, '2024-07-16'),
('123412344', 21, '2024-07-16');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `riesgocritico`
--

CREATE TABLE `riesgocritico` (
  `id_riesgoCritico` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `pregunta` int(11) NOT NULL,
  `respuesta_correcta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `riesgocritico`
--

INSERT INTO `riesgocritico` (`id_riesgoCritico`, `nombre`, `pregunta`, `respuesta_correcta`) VALUES
(1, 'CONTACTO CON ENERGÍA \nELÉCTRICA', 5, 1),
(2, 'CAÍDA DISTINTO NIVEL', 5, 1),
(3, 'APLASTAMIENTO / ATRAPAMIENTO POR CARGA SUSPENDIDA', 6, 1),
(4, 'PROYECCIÓN DESCONTROLADA DE LÍQUIDOS A ALTA PRESIÓN O FLUJO DE AIRE COMPRIMIDO', 4, 1),
(5, 'CAÍDA DE ROCA A CIELO ABIERTO', 5, 1),
(6, 'INCENDIO', 5, 1),
(7, 'CONTACTO CON SUSTANCIAS QUÍMICAS PELIGROSAS', 7, 1),
(9, 'ATRAPAMIENTO / APRISIONAMIENTO CON PARTES MÓVILES', 3, 1),
(10, 'CHOQUE / COLISIÓN / VOLCAMIENTO DE VEHÍCULO', 4, 1),
(11, 'EXPOSICIÓN A ATMÓSFERAS PELIGROSAS EN ESPACIOS CONFINADOS', 5, 1),
(12, 'CONTACTO CON MATERIAL FUNDIDO', 1, 1),
(13, 'CAÍDA DE OBJETOS HERRAMIENTAS O ESTRUCTURAS DE DISTINTO NIVEL', 4, 1),
(16, 'CAÍDA A PIQUES', 4, 1),
(18, 'APLASTAMIENTO / ATRAPAMIENTO POR CAÍDA DE ROCAS EN MINA SUBTERRÁNEA', 5, 1),
(19, 'ESTALLIDO DE ROCA', 5, 1),
(20, 'CONCENTRACIÓN AMBIENTAL PELIGROSA DE POLVO Y SÍLICE', 3, 1),
(22, 'DEFORMACIÓN INESTABILIDAD Y COLAPSO DE COMPONENTES EN PASILLOS PISOS Y BARANDAS', 3, 1),
(23, 'COLAPSO ESTRUCTURAL EN MINA SUBTERRÁNEA', 3, 1),
(24, 'DESPRENDIMIENTO Y CAÍDA DE TALUD EN MINA CIELO ABIERTO', 3, 1),
(25, 'CHOQUE / COLISIÓN / VOLCAMIENTO DE MAQUINARIAS', 3, 1),
(26, 'CHOQUE / COLISIÓN / VOLCAMIENTO DE EQUIPOS AUTÓNOMOS', 6, 1),
(27, 'ATROPELLO', 5, 1),
(28, 'AIRBLAST (GOLPE DE AIRE)', 4, 1);

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
-- Indices de la tabla `incorpora`
--
ALTER TABLE `incorpora`
  ADD KEY `incorpora_FK` (`id_art`),
  ADD KEY `incorpora_FK_1` (`id_pregunta`);

--
-- Indices de la tabla `posee`
--
ALTER TABLE `posee`
  ADD KEY `id_actividad` (`id_actividad`),
  ADD KEY `id_riesgoCritico` (`id_riesgoCritico`);

--
-- Indices de la tabla `pregunta`
--
ALTER TABLE `pregunta`
  ADD PRIMARY KEY (`id_pregunta`);

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
  MODIFY `id_actividad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `art`
--
ALTER TABLE `art`
  MODIFY `id_ART` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `pregunta`
--
ALTER TABLE `pregunta`
  MODIFY `id_pregunta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `riesgocritico`
--
ALTER TABLE `riesgocritico`
  MODIFY `id_riesgoCritico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `art`
--
ALTER TABLE `art`
  ADD CONSTRAINT `art_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `actividad` (`id_actividad`);

--
-- Filtros para la tabla `incorpora`
--
ALTER TABLE `incorpora`
  ADD CONSTRAINT `incorpora_FK` FOREIGN KEY (`id_art`) REFERENCES `art` (`id_ART`),
  ADD CONSTRAINT `incorpora_FK_1` FOREIGN KEY (`id_pregunta`) REFERENCES `pregunta` (`id_pregunta`);

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
