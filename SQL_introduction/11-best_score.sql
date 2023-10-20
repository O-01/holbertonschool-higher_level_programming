-- lists all records with score >= 10 in table second_table of db hbtn_0c_0
-- score, name - entries sorted by highest score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
