-- creates the table force_name on your MySQL server if not already there
-- VALUES: id INT name VARCHAR(256)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256)
);