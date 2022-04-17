-- ------------------------------------------------------------------------
-- Datenbank Zeiterfassung
-- ------------------------------------------------------------------------
DROP DATABASE IF EXISTS Zeiterfassung;
CREATE DATABASE IF NOT EXISTS Zeiterfassung;
CREATE SCHEMA IF NOT EXISTS `Zeiterfassung` DEFAULT CHARACTER SET utf8mb4;
USE `Zeiterfassung` ;

-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Person'
-- -----------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `Person` (
  `person_id` VARCHAR(45) NOT NULL ,
  `vorname` VARCHAR(45) NULL,
  `nachname` VARCHAR(45) NULL,
  `mail_adresse` VARCHAR(150) NULL,
  `benutzername` VARCHAR(150) NULL,
  `urlaubstage` INT NULL,
  `ueberstunden` INT NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`person_id`));
  
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Aktivitaet'
-- -----------------------------------------------------------------------
  CREATE TABLE IF NOT EXISTS `Aktivitaet` (
  `aktivitaet_id` VARCHAR(45) NOT NULL ,
  `bezeichnung` VARCHAR(45) NOT NULL ,
  `dauer` INT NULL,
  `kapazitaet` INT NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`aktivitaet_id`));
  
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Projekt'
-- -----------------------------------------------------------------------  
  CREATE TABLE IF NOT EXISTS `Projekt` (
  `projekt_id` VARCHAR(45) NOT NULL ,
  `person_id` VARCHAR(45) NOT NULL ,
  `auftraggeber` VARCHAR(150) NULL,
  `kapazitaet` INT NULL,
  `dauer` INT NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`projekt_id`),
  FOREIGN KEY (`person_id`)
	REFERENCES `Person` (`person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  
  
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Urlaub'
-- -----------------------------------------------------------------------
   CREATE TABLE IF NOT EXISTS `Urlaub` (
  `urlaub_id` VARCHAR(45) NOT NULL ,
  `projekt_id` VARCHAR(45) NOT NULL ,
  `person_id` VARCHAR(45) NOT NULL ,
  `start_datum` DATETIME NULL,
  `end_datum` DATETIME NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`urlaub_id`),
	FOREIGN KEY (`projekt_id`)
	REFERENCES `Projekt` (`projekt_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`person_id`)
    REFERENCES `Person` (`person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Pause'
-- -----------------------------------------------------------------------
   CREATE TABLE IF NOT EXISTS `Pause` (
  `pause_id` VARCHAR(45) NOT NULL ,
  `projekt_id` VARCHAR(45) NOT NULL ,
  `person_id` VARCHAR(45) NOT NULL ,
  `pause_start` DATETIME NULL,
  `pause_ende` DATETIME NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`pause_id`),
	FOREIGN KEY (`projekt_id`)
	REFERENCES `Projekt` (`projekt_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`person_id`)
    REFERENCES `Person` (`person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
  
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Zeitintervallbuchung'
-- -----------------------------------------------------------------------
   CREATE TABLE IF NOT EXISTS `Zeitintervallbuchung` (
  `zeit_id` VARCHAR(45) NOT NULL ,
  `projekt_id` VARCHAR(45) NOT NULL ,
  `person_id` VARCHAR(45) NOT NULL ,
  `aktivitaet_id` VARCHAR(45) NOT NULL ,
  `zeit_start` DATETIME NULL,
  `zeit_ende` DATETIME NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`zeit_id`),
	FOREIGN KEY (`projekt_id`)
	REFERENCES `Projekt` (`projekt_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`person_id`)
    REFERENCES `Person` (`person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`aktivitaet_id`)
    REFERENCES `Aktivitaet` (`aktivitaet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);  
    
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Arbeitszeitkonto'
-- -----------------------------------------------------------------------
   CREATE TABLE IF NOT EXISTS `Arbeitszeitkonto` (
  `zeit_id` VARCHAR(45) NOT NULL ,
  `person_id` VARCHAR(45) NOT NULL ,
  `zeit_gesamt` INT NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`person_id`,`zeit_id`),
	FOREIGN KEY (`person_id`)
	REFERENCES `Person` (`person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`zeit_id`)
    REFERENCES `Zeitintervallbuchung` (`zeit_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);  
    
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Aktivitaet_in_Projekt'
-- -----------------------------------------------------------------------
   CREATE TABLE IF NOT EXISTS `Aktivitaet_in_Projekt` (
  `aktivitaet_id` VARCHAR(45) NOT NULL ,
  `projekt_id` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`aktivitaet_id`,`projekt_id`),
	FOREIGN KEY (`aktivitaet_id`)
	REFERENCES `Aktivitaet` (`aktivitaet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`projekt_id`)
    REFERENCES `Projekt` (`projekt_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);  
    
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Mitarbeiter_in_Projekt'
-- -----------------------------------------------------------------------
   CREATE TABLE IF NOT EXISTS `Mitarbeiter_in_Projekt` (
  `person_id` VARCHAR(45) NOT NULL ,
  `projekt_id` VARCHAR(45) NOT NULL ,
  `verkaufte_stunden` INT NULL,
  PRIMARY KEY (`person_id`,`projekt_id`),
	FOREIGN KEY (`person_id`)
	REFERENCES `Person` (`person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`projekt_id`)
    REFERENCES `Projekt` (`projekt_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);  
  
  
  
-- ---------------------------------------------------------------------------------------------------------------------------
-- Person Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Person` (person_id, vorname, nachname, mail_adresse, benutzername, urlaubstage, ueberstunden, letzte_aenderung)  
VALUES('1', 'Talha', 'Yildirim', 'talha.windows@gmail.com', 'Karen', 365, 0, '2022-04-13 02:30:00');
INSERT INTO `Person` (person_id, vorname, nachname, mail_adresse, benutzername, urlaubstage, ueberstunden, letzte_aenderung)  
VALUES('2', 'Aykut', 'Demir', 'kafabey@hotmail.de', 'Kafa Bey', 365, 0, '2022-04-13 02:30:00');

-- --------------------------------------------------------------------------------------------------------------------------
-- Tabelle 'Person' anzeigen
-- --------------------------------------------------------------------------------------------------------------------------
-- SELECT * FROM `Person`;
SELECT * FROM `Mitarbeiter_in_Projekt`;
SELECT * FROM `Aktivitaet`;
