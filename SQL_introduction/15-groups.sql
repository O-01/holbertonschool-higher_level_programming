-- lists no. of records with same score in table second_table of db hbtn_0c_0
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
