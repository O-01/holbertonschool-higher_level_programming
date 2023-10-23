-- lists all cities contained in the database hbtn_0d_usa
-- should display: cities.id - cities.name - states.name
-- sorted in ascending order by cities.id
-- only 1 SELECT statement used
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
