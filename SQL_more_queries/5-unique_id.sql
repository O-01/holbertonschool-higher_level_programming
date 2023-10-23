-- creates the table unique_id on your MySQL server if not already there
-- id INT DEFAULT 1 UNIQUE, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
