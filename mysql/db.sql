-- ------------------------------------------------------------------------
-- Datenbank Zeiterfassung
-- ------------------------------------------------------------------------
DROP DATABASE IF EXISTS Zeiterfassung;
CREATE DATABASE IF NOT EXISTS Zeiterfassung DEFAULT CHARACTER SET utf8mb4;
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
  `dauer` DATETIME NULL,
  `kapazitaet` INT NULL,
  `letzte_aenderung` DATETIME NULL,
  PRIMARY KEY (`aktivitaet_id`));
  
-- -----------------------------------------------------------------------
-- Tabelle erstellen 'Projekt'
-- -----------------------------------------------------------------------  
  CREATE TABLE IF NOT EXISTS `Projekt` (
  `projekt_id` VARCHAR(45) NOT NULL ,
  `person_id` VARCHAR(45) NOT NULL ,
  `projektname` VARCHAR(150) NULL,
  `auftraggeber` VARCHAR(150) NULL,
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
  `aktivitaet_idd` VARCHAR(45) NOT NULL ,
  `projekt_id` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`aktivitaet_idd`,`projekt_id`),
	FOREIGN KEY (`aktivitaet_idd`)
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

-- ---------------------------------------------------------------------------------------------------------------------------
-- Projekt Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Projekt` (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung)  
VALUES('1', '1',"Projekt X", 'Daimler','2022-04-19 02:33:00');
INSERT INTO `Projekt` (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung)  
VALUES('2', '2',"Projekt Y", 'Porsche','2022-04-19 12:33:00');

-- ---------------------------------------------------------------------------------------------------------------------------
-- Aktivität Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Aktivitaet` (aktivitaet_id, bezeichnung, dauer, kapazitaet, letzte_aenderung)  
VALUES('1', 'Klassendiagram erstellen', '2022-04-30 14:00:00','120', '2022-04-19 02:33:00');
INSERT INTO `Aktivitaet` (aktivitaet_id, bezeichnung, dauer, kapazitaet, letzte_aenderung)  
VALUES('2', 'Datenbankentwurf erstellen', '2022-05-01 14:00:00','100', '2022-04-19 02:33:00');
INSERT INTO `Aktivitaet` (aktivitaet_id, bezeichnung, dauer, kapazitaet, letzte_aenderung)  
VALUES('3', 'Rechnung schreiben', '2022-05-01 14:00:00','100', '2022-04-19 02:33:00');

-- ---------------------------------------------------------------------------------------------------------------------------
-- Aktivität_in_Projekt Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Aktivitaet_in_Projekt` (aktivitaet_idd, projekt_id)  
VALUES('1', '1');
INSERT INTO `Aktivitaet_in_Projekt` (aktivitaet_idd, projekt_id)  
VALUES('2', '1');
INSERT INTO `Aktivitaet_in_Projekt` (aktivitaet_idd, projekt_id)  
VALUES('3', '2');

-- --------------------------------------------------------------------------------------------------------------------------
-- Auslesen von Projekten und den zugehörigen Ativitäten, durch den INNER JOIN Befehl 
-- --------------------------------------------------------------------------------------------------------------------------

-- SELECT bezeichnung, projekt_id FROM Aktivitaet INNER JOIN Aktivitaet_in_Projekt
-- WHERE aktivitaet_idd = aktivitaet_id AND projekt_id = 1;
	




