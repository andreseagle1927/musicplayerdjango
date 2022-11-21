-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema laboratorio_software
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema laboratorio_software
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `laboratorio_software` DEFAULT CHARACTER SET utf8 ;
USE `laboratorio_software` ;

-- -----------------------------------------------------
-- Table `laboratorio_software`.`Cantante`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `laboratorio_software`.`Cantante` ;

CREATE TABLE IF NOT EXISTS `laboratorio_software`.`Cantante` (
  `idCantante` INT NOT NULL AUTO_INCREMENT,
  `nombreCantante` VARCHAR(45) NULL,
  `pais` VARCHAR(45) NULL,
  `edad` VARCHAR(45) NULL,
  PRIMARY KEY (`idCantante`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `laboratorio_software`.`Canciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `laboratorio_software`.`Canciones` ;

CREATE TABLE IF NOT EXISTS `laboratorio_software`.`Canciones` (
  `idCancion` INT GENERATED ALWAYS AS () VIRTUAL,
  `id_cantante` INT NOT NULL,
  `nombreCancion` VARCHAR(45) NOT NULL,
  `genero` VARCHAR(45) NULL,
  `duracion` VARCHAR(45) NULL,
  `link` VARCHAR(500) NULL,
  `plays` INT ZEROFILL NULL,
  PRIMARY KEY (`idCancion`),
  INDEX `fk_Canciones_Cantante1_idx` (`id_cantante` ASC) VISIBLE,
  CONSTRAINT `fk_Canciones_Cantante1`
    FOREIGN KEY (`id_cantante`)
    REFERENCES `laboratorio_software`.`Cantante` (`idCantante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `laboratorio_software`.`Ranking`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `laboratorio_software`.`Ranking` ;

CREATE TABLE IF NOT EXISTS `laboratorio_software`.`Ranking` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `laboratorio_software`.`AsignacionRanking`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `laboratorio_software`.`AsignacionRanking` ;

CREATE TABLE IF NOT EXISTS `laboratorio_software`.`AsignacionRanking` (
  `idAsignacion` INT NOT NULL,
  `Ranking_id` INT NOT NULL,
  `Canciones_idCancion` INT NOT NULL,
  INDEX `fk_table1_Ranking1_idx` (`Ranking_id` ASC) VISIBLE,
  INDEX `fk_table1_Canciones1_idx` (`Canciones_idCancion` ASC) VISIBLE,
  PRIMARY KEY (`idAsignacion`),
  CONSTRAINT `fk_table1_Ranking1`
    FOREIGN KEY (`Ranking_id`)
    REFERENCES `laboratorio_software`.`Ranking` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_table1_Canciones1`
    FOREIGN KEY (`Canciones_idCancion`)
    REFERENCES `laboratorio_software`.`Canciones` (`idCancion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
