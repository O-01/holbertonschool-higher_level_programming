-- creates table "first_table" in the current database in MySQL server
-- id INT
-- name VARCHAR(256)
-- should not fail if table named "first_table" already exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
