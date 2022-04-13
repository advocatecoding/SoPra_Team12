-- ------------------------------------------------------------------------
-- Datenbank Zeiterfassung
-- ------------------------------------------------------------------------
DROP DATABASE IF EXISTS Zeiterfassung;
CREATE DATABASE IF NOT EXISTS Zeiterfassung;
CREATE SCHEMA IF NOT EXISTS `Zeiterfassung` DEFAULT CHARACTER SET utf8 ;
USE `Zeiterfassung` ;

-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Person'
-- -----------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `Person` (
  `person_id` VARCHAR(45) NOT NULL ,
  `vorname` VARCHAR(45) NULL,
  `nachname` VARCHAR(45) NULL,
  `Mail_Adresse` VARCHAR(150) NULL,
  `Benutzername` VARCHAR(150) NULL,
  `Urlaubstage` INT NULL,
  `Überstunden` INT NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`person_id`));

-- ---------------------------------------------------------------------------------------------------------------------------
-- Person Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Person` (person_id, vorname, nachname, Mail_Adresse, Benutzername, Urlaubstage, Überstunden, letzte_aenderung)  
VALUES('1', 'Talha', 'Yildirim', 'talha.windows@gmail.com', 'Karen', 365, 0, '2022-04-13 02:30:00');
INSERT INTO `Person` (person_id, vorname, nachname, Mail_Adresse, Benutzername, Urlaubstage, Überstunden, letzte_aenderung)  
VALUES('2', 'Aykut', 'Demir', 'kafabey@hotmail.de', 'Kafa Bey', 365, 0, '2022-04-13 02:30:00');

-- --------------------------------------------------------------------------------------------------------------------------
-- Tabelle 'Person' anzeigen
-- --------------------------------------------------------------------------------------------------------------------------
SELECT * FROM `Person`;
