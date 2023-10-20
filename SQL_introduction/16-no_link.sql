-- lists all records of table second_table of db hbtn_0c_0 having name entry
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
