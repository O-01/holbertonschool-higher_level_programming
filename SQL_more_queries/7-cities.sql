-- creates database hbtn_0d_usa if not already existing
-- creates the table cities on hbtn_0d_usa if not already there
-- id INT NOT NULL UNIQUE PRIMARY KEY, AUTO GENERATED
-- state_id INT NOT NULL FOREIGN KEY states(id)
-- name VARCHAR(256) NOT NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL UNIQUE,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
