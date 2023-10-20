-- lists no. of records with same score in table second_table of db hbtn_0c_0
SELECT score, COUNT(score) as number FROM second_table ORDER BY score DESC;
