-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-07-2024 a las 23:21:52
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
  `Contexto_trab_simultaneo` varchar(150) NOT NULL,
  `coordinacion_lider` tinyint(1) NOT NULL,
  `verificacion_controles_criticos` tinyint(1) NOT NULL,
  `comunicacion_trabajadores_control` tinyint(1) NOT NULL,
  `id_actividad` int(11) NOT NULL,
  `estado_trabajador` tinyint(1) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_termino` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `art`
--

INSERT INTO `art` (`id_ART`, `trabajo_simultaneo`, `Contexto_trab_simultaneo`, `coordinacion_lider`, `verificacion_controles_criticos`, `comunicacion_trabajadores_control`, `id_actividad`, `estado_trabajador`, `hora_inicio`, `hora_termino`) VALUES
(1, 1, 'nuevo_valor_contexto', 1, 1, 1, 1, 1, '00:00:00', '00:00:00'),
(2, 0, 'x,d,x,d,x,d', 0, 1, 0, 2, 1, '00:00:00', '00:00:00'),
(3, 0, '', 0, 0, 0, 1, 0, '00:00:00', '00:00:00'),
(4, 1, '', 0, 0, 0, 4, 1, '00:00:00', '00:00:00'),
(5, 1, '', 0, 0, 0, 3, 0, '00:00:00', '00:00:00'),
(6, 1, '', 0, 0, 0, 1, 1, '22:26:21', '00:18:00'),
(7, 1, '', 0, 0, 0, 1, 1, '22:29:19', '00:18:00'),
(8, 1, '', 0, 0, 0, 1, 1, '22:29:24', '00:18:00'),
(9, 1, '', 0, 0, 0, 1, 1, '22:29:50', '00:18:00'),
(10, 1, '', 0, 0, 0, 1, 1, '22:30:26', '00:18:00'),
(11, 1, '', 0, 0, 0, 1, 1, '22:30:26', '00:18:00'),
(12, 1, '', 0, 0, 0, 1, 1, '22:31:14', '00:18:00'),
(13, 1, '', 0, 0, 0, 1, 1, '22:31:14', '00:18:00'),
(14, 1, '', 0, 0, 0, 1, 1, '22:34:40', '24:18:00'),
(15, 1, '', 0, 0, 0, 1, 1, '22:41:01', '24:18:00'),
(16, 1, '', 0, 0, 0, 1, 1, '22:46:57', '18:27:00'),
(18, 1, '', 0, 0, 0, 3, 1, '23:29:21', '20:00:00'),
(19, 1, '', 0, 0, 0, 3, 1, '23:30:47', '20:00:00'),
(20, 1, '', 0, 0, 0, 3, 1, '01:37:11', '20:00:00'),
(21, 1, '', 0, 0, 0, 3, 1, '22:08:28', '20:00:00'),
(22, 1, '', 0, 0, 0, 3, 1, '17:32:20', '20:00:00'),
(23, 1, '', 0, 0, 0, 5, 1, '17:44:55', '20:00:00'),
(24, 1, '', 0, 0, 0, 5, 1, '17:44:55', '20:00:00'),
(25, 1, '', 0, 0, 0, 1, 1, '17:50:04', '20:00:00'),
(27, 1, '', 0, 0, 0, 3, 1, '20:40:45', '20:00:00'),
(28, 1, '', 0, 0, 0, 3, 1, '20:52:21', '20:00:00'),
(29, 1, '', 0, 0, 0, 3, 1, '21:00:29', '00:00:00'),
(30, 1, '', 0, 0, 0, 3, 1, '21:01:29', '20:00:00'),
(31, 1, '', 0, 0, 0, 3, 1, '21:03:30', '08:00:00'),
(32, 1, '', 0, 0, 0, 3, 1, '21:07:20', '08:00:00'),
(33, 1, '', 0, 0, 0, 5, 1, '21:09:10', '08:00:00'),
(34, 1, '', 0, 0, 0, 3, 1, '21:16:30', '08:00:00'),
(35, 1, '', 0, 0, 0, 5, 1, '05:27:25', '08:00:00'),
(36, 1, '', 0, 0, 0, 5, 1, '05:29:03', '08:00:00'),
(37, 1, '', 0, 0, 0, 5, 1, '05:42:44', '08:00:00'),
(38, 1, '', 0, 0, 0, 2, 1, '13:01:14', '20:00:00'),
(39, 1, '', 0, 0, 0, 2, 1, '13:01:14', '20:00:00'),
(40, 1, '', 0, 0, 0, 2, 1, '13:01:14', '20:00:00'),
(41, 1, '', 0, 0, 0, 2, 1, '13:01:14', '20:00:00'),
(42, 1, '', 0, 0, 0, 2, 1, '13:01:14', '20:00:00'),
(43, 1, '', 0, 0, 0, 3, 1, '15:44:12', '20:00:00'),
(44, 1, '', 0, 0, 0, 3, 1, '15:45:57', '20:00:00'),
(45, 1, 'Trabajo junto a personal de as', 1, 1, 1, 3, 1, '15:55:06', '20:00:00'),
(46, 0, '', 0, 0, 0, 5, 0, '21:12:26', '20:00:00'),
(47, 0, '', 0, 0, 0, 5, 0, '21:15:45', '20:00:00'),
(48, 0, 'N,o, ,e,x,i,s,t,e, ,t,r,a,b,a,j,o, ,s,i,m,u,l,t,a,n,e,o', 0, 0, 0, 5, 1, '21:19:24', '20:00:00'),
(49, 0, 'No,existe,trabajo,simultaneo', 0, 0, 0, 5, 0, '21:22:34', '08:00:00'),
(50, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 0, '21:33:00', '20:00:00'),
(51, 0, '', 0, 0, 0, 5, 0, '23:11:22', '20:00:00'),
(52, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 5, 0, '23:14:24', '20:00:00'),
(53, 0, '', 0, 0, 0, 5, 0, '23:57:42', '20:00:00'),
(54, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 5, 1, '00:06:48', '20:00:00'),
(55, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 1, 0, '00:07:42', '08:00:00'),
(56, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 1, 0, '00:16:40', '20:00:00'),
(57, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 3, 0, '00:49:48', '20:00:00'),
(58, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 0, '00:51:39', '20:00:00'),
(59, 0, 'No existe trabajo simultaneo', 0, 0, 0, 5, 0, '00:57:53', '20:00:00'),
(60, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 1, '01:05:29', '20:00:00'),
(61, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 0, '01:06:15', '20:00:00'),
(62, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 3, 1, '01:46:50', '08:00:00'),
(63, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 5, 1, '01:47:52', '08:00:00'),
(64, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 0, '09:19:42', '20:00:00'),
(65, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 0, '09:34:34', '20:00:00'),
(66, 1, 'Trabajo en equipo', 1, 1, 1, 3, 1, '16:17:09', '20:00:00'),
(67, 1, 'Trabajo junto a personal de aseo,Trabajo sala compartida,Trabajo en equipo,Trabajo entre actividades', 1, 1, 1, 3, 1, '16:18:10', '20:00:00'),
(68, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 1, '16:20:10', '20:00:00'),
(69, 0, 'No existe trabajo simultaneo', 0, 0, 0, 3, 1, '17:00:06', '20:00:00');

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
  `contraseña` varchar(33) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`rut`, `nombre_completo`, `correo`, `telefono`, `direccion_residencia`, `cargo`, `especialidad`, `contraseña`) VALUES
('123412344', 'Patricio la Estrella', 'patricioSexy@gmail.com', '956528381', 'en una piedra bajo del mar', 'Trabajador', 'Estrella de mar', 'qwerqwer'),
('123456789', 'Alvaro Vergara', 'elperroloco@gmail.com', '222222222', 'antofa', 'Supervisor', '', 'Alvaricoque'),
('187697653', 'Carolina Ramirez', 'Carolina123@gmail.com', '989976554', 'vasco de gama', 'Supervisor', 'XD', '4d186321c1a7f0f354b297e8914ab240'),
('187888853', 'pedro', 'pedro@gmail.com', '98746767', 'canada', 'Supervisor', 'Nada', 'asdfasdf'),
('208971234', 'Vladimir Heriquez ', 'Vladimir@gmail.com', '978653454', 'tres', 'Trabajador', 'Químico analista', 'vladimmir1234'),
('218679323', 'Margarita cordera', 'margarita@gmail.com', '73378556', 'uno', 'Trabajador', 'Tec, Quimico', 'maar123'),
('224750987', 'Karen Herrera', 'Karen12@gmail.com', '941281473', 'cero', 'Trabajador', 'Auxliar Lavado', 'Karen123'),
('236980472', 'Checo Perez', 'Chequito@gmail.com', '+579524256', 'Le mans', 'Supervisor', '', 'Samuel123'),
('76564345', 'no c', '12345@gmail.com', '98765432', 'no se', 'Trabajador', 'holaPrueba', 'asdfasdf'),
('765787894', 'Alexander', 'dasdjkh@gmail.com', '58956254', 'Francia', 'Trabajador', 'Todo', '4d186321c1a7f0f354b297e8914ab240'),
('87698554k', 'pablo perez', 'pablo@gmail.com', '67489667', 'España', 'Trabajador', 'Nada x2', 'abcdfghi');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `incorpora`
--

CREATE TABLE `incorpora` (
  `id_art` int(11) NOT NULL,
  `id_pregunta` int(11) NOT NULL,
  `respuesta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `incorpora`
--

INSERT INTO `incorpora` (`id_art`, `id_pregunta`, `respuesta`) VALUES
(25, 1, 1),
(25, 1, 1),
(25, 2, 1),
(25, 3, 1),
(25, 4, 1),
(25, 5, 1),
(25, 6, 1),
(25, 1, 1),
(25, 2, 1),
(25, 3, 1),
(25, 4, 1),
(25, 5, 1),
(25, 6, 1),
(34, 1, 1),
(34, 2, 1),
(34, 3, 1),
(34, 4, 1),
(34, 5, 1),
(34, 6, 1),
(34, 1, 1),
(34, 2, 1),
(34, 3, 1),
(34, 4, 1),
(34, 5, 1),
(34, 6, 1),
(34, 1, 1),
(34, 2, 1),
(34, 3, 1),
(34, 4, 1),
(34, 5, 1),
(34, 6, 1),
(34, 7, 1),
(34, 8, 1),
(34, 9, 1),
(34, 10, 1),
(34, 11, 1),
(34, 12, 1),
(22, 7, 1),
(22, 8, 1),
(22, 9, 1),
(22, 10, 1),
(22, 11, 1),
(22, 12, 1),
(35, 1, 1),
(35, 2, 1),
(35, 3, 1),
(35, 4, 1),
(35, 5, 1),
(35, 6, 1),
(36, 1, 1),
(36, 2, 1),
(36, 3, 1),
(36, 4, 1),
(36, 5, 1),
(36, 6, 1),
(37, 1, 1),
(37, 2, 1),
(37, 3, 1),
(37, 4, 1),
(37, 5, 1),
(37, 6, 1),
(36, 7, 1),
(36, 8, 1),
(36, 9, 1),
(36, 10, 1),
(36, 11, 1),
(36, 12, 1),
(1, 7, 1),
(1, 8, 1),
(1, 9, 1),
(1, 10, 1),
(1, 11, 1),
(1, 12, 1),
(37, 7, 1),
(37, 8, 1),
(37, 9, 1),
(37, 10, 1),
(37, 11, 1),
(37, 12, 1),
(38, 1, 1),
(38, 2, 1),
(38, 3, 1),
(38, 4, 1),
(38, 5, 1),
(38, 6, 1),
(39, 1, 1),
(39, 2, 1),
(39, 3, 1),
(39, 4, 1),
(39, 5, 1),
(39, 6, 1),
(40, 1, 1),
(40, 2, 1),
(40, 3, 1),
(40, 4, 1),
(40, 5, 1),
(40, 6, 1),
(41, 1, 1),
(41, 2, 1),
(41, 3, 1),
(41, 4, 1),
(41, 5, 1),
(41, 6, 1),
(42, 1, 1),
(42, 2, 1),
(42, 3, 1),
(42, 4, 1),
(42, 5, 1),
(42, 6, 1),
(42, 7, 1),
(42, 8, 1),
(42, 9, 1),
(42, 10, 1),
(42, 11, 1),
(42, 12, 1),
(42, 7, 1),
(42, 8, 1),
(42, 9, 1),
(42, 10, 1),
(42, 11, 1),
(42, 12, 1),
(42, 7, 1),
(42, 8, 1),
(42, 9, 1),
(42, 10, 1),
(42, 11, 1),
(42, 12, 1),
(42, 7, 1),
(42, 8, 1),
(42, 9, 1),
(42, 10, 1),
(42, 11, 1),
(42, 12, 1),
(42, 7, 1),
(42, 8, 1),
(42, 9, 1),
(42, 10, 1),
(42, 11, 1),
(42, 12, 1),
(43, 1, 1),
(43, 2, 1),
(43, 3, 1),
(43, 4, 1),
(43, 5, 1),
(43, 6, 1),
(44, 1, 1),
(44, 2, 1),
(44, 3, 1),
(44, 4, 1),
(44, 5, 1),
(44, 6, 1),
(45, 1, 1),
(45, 2, 1),
(45, 3, 1),
(45, 4, 1),
(45, 5, 1),
(45, 6, 1),
(46, 1, 1),
(46, 2, 1),
(46, 3, 1),
(46, 4, 1),
(46, 5, 1),
(46, 6, 1),
(47, 1, 1),
(47, 2, 1),
(47, 3, 1),
(47, 4, 1),
(47, 5, 1),
(47, 6, 1),
(48, 1, 1),
(48, 2, 1),
(48, 3, 1),
(48, 4, 1),
(48, 5, 1),
(48, 6, 1),
(49, 1, 1),
(49, 2, 1),
(49, 3, 1),
(49, 4, 1),
(49, 5, 1),
(49, 6, 1),
(50, 1, 1),
(50, 2, 1),
(50, 3, 1),
(50, 4, 1),
(50, 5, 1),
(50, 6, 1),
(52, 1, 1),
(52, 2, 1),
(52, 3, 1),
(52, 4, 1),
(52, 5, 1),
(52, 6, 1),
(54, 1, 1),
(54, 2, 1),
(54, 3, 1),
(54, 4, 1),
(54, 5, 1),
(54, 6, 1),
(55, 1, 1),
(55, 2, 1),
(55, 3, 1),
(55, 4, 1),
(55, 5, 1),
(55, 6, 1),
(56, 1, 1),
(56, 2, 1),
(56, 3, 1),
(56, 4, 1),
(56, 5, 1),
(56, 6, 1),
(57, 1, 1),
(57, 2, 1),
(57, 3, 1),
(57, 4, 1),
(57, 5, 1),
(57, 6, 1),
(58, 1, 1),
(58, 2, 1),
(58, 3, 1),
(58, 4, 1),
(58, 5, 1),
(58, 6, 1),
(59, 1, 1),
(59, 2, 1),
(59, 3, 1),
(59, 4, 1),
(59, 5, 1),
(59, 6, 1),
(60, 1, 1),
(60, 2, 1),
(60, 3, 1),
(60, 4, 1),
(60, 5, 1),
(60, 6, 1),
(61, 1, 1),
(61, 2, 1),
(61, 3, 1),
(61, 4, 1),
(61, 5, 1),
(61, 6, 1),
(62, 1, 1),
(62, 2, 1),
(62, 3, 1),
(62, 4, 1),
(62, 5, 1),
(62, 6, 1),
(63, 1, 1),
(63, 2, 1),
(63, 3, 1),
(63, 4, 1),
(63, 5, 1),
(63, 6, 1),
(66, 1, 1),
(66, 2, 1),
(66, 3, 1),
(66, 4, 1),
(66, 5, 1),
(66, 6, 1),
(67, 1, 1),
(67, 2, 1),
(67, 3, 1),
(67, 4, 1),
(67, 5, 1),
(67, 6, 1),
(68, 1, 1),
(68, 2, 1),
(68, 3, 1),
(68, 4, 1),
(68, 5, 1),
(68, 6, 1);

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
  `cargo` varchar(45) NOT NULL,
  `respuesta_correcta` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pregunta`
--

INSERT INTO `pregunta` (`id_pregunta`, `descripcion`, `cargo`, `respuesta_correcta`) VALUES
(1, '¿El trabajo que asignaré cuenta con un estándar, procedimiento y/o instructivo?', 'Supervisor', 1),
(2, '¿El personal que asignaré para realizar el trabajo, cuenta con las capacitaciones, \r\ncompetencias, salud compatible y/o acreditaciones requeridas?', 'Supervisor', 1),
(3, '¿Durante la planificación del trabajo, me aseguro de solicitar los permisos para \ningresar a las áreas, intervenir equipos y/o interactuar con energías?', 'Supervisor', 1),
(4, 'Verifiqué que el personal cuenta con los elementos requeridos para realizar la \nsegregación y señalización del área de trabajo, según diseño?', 'Supervisor', 1),
(5, '¿El personal a mi cargo cuenta con sistema de comunicación de acuerdo al \r\nprotocolo de emergencia del área?', 'Supervisor', 1),
(6, '¿El personal que asignaré para realizar el trabajo, cuenta con los EPP definidos en \r\nel procedimiento de trabajo?', 'Supervisor', 1),
(7, '¿Conozco el estándar, procedimiento y/o instructivo del trabajo que ejecutaré?', 'Trabajador', 1),
(8, '¿Cuento con las competencias y salud compatible para ejecutar el trabajo?', 'Trabajador', 1),
(9, '¿Cuento con la autorización para ingresar al área a ejecutar el trabajo?', 'Trabajador', 1),
(10, '¿Segregué y señalicé el área de trabajo con los elementos según diseño?', 'Trabajador', 1),
(11, '¿Conozco el número de teléfono o frecuencia radial para dar aviso en caso de \r\nemergencia, según protocolo del área?', 'Trabajador', 1),
(12, '¿Uso los EPP definidos para el trabajo y se encuentran en buenas condiciones?', 'Trabajador', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `realiza`
--

CREATE TABLE `realiza` (
  `rut` char(9) NOT NULL,
  `id_ART` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado_ART` varchar(15) NOT NULL,
  `supervisor_asignado` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `realiza`
--

INSERT INTO `realiza` (`rut`, `id_ART`, `fecha`, `estado_ART`, `supervisor_asignado`) VALUES
('187697653', 1, '2024-07-15', 'pendiente', ''),
('208971234', 15, '2024-06-26', '', ''),
('208971234', 16, '2024-06-26', '', ''),
('123412344', 18, '2024-07-15', '', ''),
('123412344', 19, '2024-07-15', '', ''),
('123412344', 20, '2024-07-16', '', ''),
('123412344', 21, '2024-07-16', '', ''),
('123412344', 22, '2024-07-17', 'concluido', ''),
('123412344', 23, '2024-07-17', '', ''),
('123412344', 24, '2024-07-17', '', ''),
('123412344', 25, '2024-07-17', '', ''),
('123412344', 34, '2024-07-17', 'concluido', ''),
('123412344', 35, '2024-07-18', '', ''),
('123412344', 36, '2024-07-18', 'concluido', ''),
('123412344', 37, '2024-07-18', 'concluido', ''),
('123412344', 38, '2024-07-18', 'pendiente', ''),
('123412344', 39, '2024-07-18', 'pendiente', ''),
('123412344', 40, '2024-07-18', 'pendiente', ''),
('123412344', 41, '2024-07-18', 'pendiente', ''),
('123412344', 42, '2024-07-18', 'concluido', ''),
('123412344', 43, '2024-07-18', 'pendiente', ''),
('123412344', 44, '2024-07-18', 'pendiente', ''),
('123412344', 45, '2024-07-18', 'pendiente', ''),
('765787894', 46, '2024-07-18', 'pendiente', ''),
('765787894', 47, '2024-07-18', 'pendiente', ''),
('765787894', 48, '2024-07-18', 'pendiente', ''),
('765787894', 49, '2024-07-18', 'pendiente', ''),
('765787894', 50, '2024-07-18', 'tarjeta verd', ''),
('765787894', 51, '2024-07-18', 'tarjeta verde', ''),
('765787894', 52, '2024-07-18', 'pendiente', ''),
('765787894', 53, '2024-07-18', 'tarjeta verde', ''),
('765787894', 54, '2024-07-19', 'pendiente', ''),
('765787894', 55, '2024-07-19', 'pendiente', ''),
('765787894', 56, '2024-07-19', 'tarjeta verde', ''),
('765787894', 57, '2024-07-19', 'tarjeta verde', ''),
('765787894', 58, '2024-07-19', 'tarjeta verde', ''),
('765787894', 59, '2024-07-19', 'tarjeta verde', ''),
('765787894', 60, '2024-07-19', 'pendiente', ''),
('765787894', 61, '2024-07-19', 'tarjeta verde', ''),
('765787894', 62, '2024-07-19', 'pendiente', 'Carolina Ramirez'),
('765787894', 63, '2024-07-19', 'pendiente', 'pedro'),
('765787894', 64, '2024-07-19', 'tarjeta verde', 'pedro'),
('765787894', 65, '2024-07-19', 'Revisado', 'Carolina Ramirez'),
('765787894', 66, '2024-07-20', 'pendiente', ''),
('765787894', 67, '2024-07-20', 'pendiente', 'Carolina Ramirez'),
('765787894', 68, '2024-07-20', 'pendiente', 'Carolina Ramirez'),
('765787894', 69, '2024-07-20', 'tarjeta verde', 'Carolina Ramirez');

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
  MODIFY `id_ART` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

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
