-- uses the hbtn_0d_tvshows database to lists all genres of show Dexter
-- tv_shows table contains only one record where title = Dexter
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id =
    (SELECT id FROM tv_shows WHERE title = 'Dexter')
ORDER BY tv_genres.name ASC;
