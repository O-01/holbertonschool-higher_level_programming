-- lists all shows in hbtn_0d_tvshows with at least one genre linked
-- display tv_shows.title, tv_show_genres.genre.id
-- sort in ascending order by tv_shows.title, tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
