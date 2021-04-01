DROP DATABASE IF EXISTS `Alimentation`;
CREATE DATABASE IF NOT EXISTS `Alimentation`;
USE `Alimentation`;


CREATE TABLE IF NOT EXISTS `Category`
(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS `Product`
(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(80) NOT NULL,
    `nutriscore` char(1) NOT NULL,
    `barcode` VARCHAR(18),
    `link` VARCHAR(120) NOT NULL,
    `favorite` BOOLEAN,
    PRIMARY KEY (id)
)
ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS `Store`
(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(300) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS `Product_category`
(
    `id_product` INT UNSIGNED NOT NULL,
    `id_category` INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_product)
    REFERENCES Product(id),
    FOREIGN KEY (id_category)
    REFERENCES Category(id),
    PRIMARY KEY (id_product, id_category)
)
ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `Product_store`
(
    `id_product` INT UNSIGNED NOT NULL,
    `id_store` INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_product)
    REFERENCES Product(id),
    FOREIGN KEY (id_store)
    REFERENCES Store(id),
    PRIMARY KEY (id_product, id_store)
)
ENGINE=INNODB;
