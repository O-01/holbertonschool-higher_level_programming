-- lists all genres from hbtn_0d_tvshows, displays no. of shows linked to each
-- should display: <TV Show genre> - <Number of shows linked to this genre>
-- first column called genre
-- second column must be called number_of_shows
-- don’t display a genre that doesn’t have any shows linked
-- sorted in descending order by the number of shows linked
SELECT 
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
