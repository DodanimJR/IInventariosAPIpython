-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 15, 2021 at 05:41 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inventario`
--

-- --------------------------------------------------------

--
-- Table structure for table `empleado`
--

CREATE TABLE `empleado` (
  `nombre` varchar(100) NOT NULL,
  `codigoId` int(11) NOT NULL,
  `puesto` varchar(200) NOT NULL,
  `rol` varchar(255) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `anotacionGerente` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `empleado`
--

INSERT INTO `empleado` (`nombre`, `codigoId`, `puesto`, `rol`, `foto`, `descripcion`, `anotacionGerente`) VALUES
('Dodanim Castillo', 1, 'CEO', 'guapo', 'https://e00-expansion.uecdn.es/assets/multimedia/imagenes/2017/09/08/15048915173238.jpg', NULL, 'es un saico timido');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `nombre` varchar(100) NOT NULL,
  `codigoId` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `categoria` varchar(255) DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `anotacionGerente` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`nombre`, `codigoId`, `precio`, `categoria`, `foto`, `descripcion`, `anotacionGerente`) VALUES
('coca cola', 1, 1500, 'Bebidas', 'https://walmartcr.vtexassets.com/arquivos/ids/221071/Refresco-Coca-Cola-Original-3000ml-1-26374.jpg?v=637625315261100000', 'Bebida gaseosa', 'Vender rapido');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`codigoId`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`codigoId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `empleado`
--
ALTER TABLE `empleado`
  MODIFY `codigoId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `codigoId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
