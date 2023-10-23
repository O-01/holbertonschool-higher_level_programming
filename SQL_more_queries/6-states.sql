-- creates database hbtn_0d_usa if not already existing
-- creates the table states on hbtn_0d_usa if not already there
-- id INT DEFAULT NOT NULL UNIQUE PRIMARY KEY, AUTO GENERATED
-- name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT DEFAULT NOT NULL PRIMARY KEY,
    name VARCHAR(256) DEFAULT NOT NULL
);
