-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2025 at 03:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shop_db`
--

--
-- Dumping data for table `bestellpositionen`
--

INSERT INTO `bestellpositionen` (`bestellposition_id`, `bestellung_id`, `produkt_id`, `menge`, `einzelpreis`) VALUES
(401, 301, 101, 1, 1200.00),
(402, 301, 104, 1, 45.00),
(403, 302, 102, 2, 25.50),
(405, 304, 105, 1, 30.00);

--
-- Dumping data for table `bestellungen`
--

INSERT INTO `bestellungen` (`bestellung_id`, `kunde_id`, `bestelldatum`, `status`, `gesamtbetrag`) VALUES
(301, 201, '2023-04-01 10:30:00', 'versandt', 1245.00),
(302, 202, '2023-04-05 14:00:00', 'storniert', 60.00),
(303, 201, '2023-04-10 11:15:00', 'bearbeitet', 179.98),
(304, 203, '2023-04-12 09:00:00', 'neu', 30.00);

--
-- Dumping data for table `kategorien`
--

INSERT INTO `kategorien` (`kategorie_id`, `name`) VALUES
(1, 'Elektronik'),
(2, 'Bücher'),
(3, 'Haushalt');

--
-- Dumping data for table `kunden`
--

INSERT INTO `kunden` (`kunde_id`, `vorname`, `nachname`, `email`, `registrierungsdatum`) VALUES
(201, 'Anna', 'Müller', 'anna.mueller@example.com', '2023-01-15'),
(202, 'Max', 'Meier', 'max.meier@example.com', '2023-02-20'),
(203, 'Lena', 'Schmidt', 'lena.schmidt@example.com', '2023-03-10'),
(204, 'Tom', 'Schneider', 'tom.schneider@example.org', '2025-11-20');

--
-- Dumping data for table `produkte`
--

INSERT INTO `produkte` (`produkt_id`, `name`, `beschreibung`, `preis`, `lagerbestand`, `kategorie_id`) VALUES
(101, 'Laptop X', 'Leistungsstarker Laptop für professionelle Anwendungen', 1200.00, 50, 1),
(102, 'Bestseller Roman', 'Spannender Roman eines bekannten Autors', 28.05, 200, 2),
(104, 'Webcam HD', 'Full HD Webcam für Videokonferenzen', 45.00, 100, 1),
(105, 'Kochbuch \"Vegane Küche\"', 'Umfassendes Kochbuch mit veganen Rezepten', 33.00, 150, 2),
(106, 'Gaming Maus Pro', 'Ergonomische Maus für Gamer mit anpassbaren Tasten', 75.99, 75, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
