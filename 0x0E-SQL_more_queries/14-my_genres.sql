-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT genres.name FROM tv_genres AS genres
INNER JOIN tv_show_genres AS shows ON genres.id = shows.genre_id

INNER JOIN tv_shows AS tv_shows ON tv_shows.id = shows.show_id
WHERE tv_shows.title = "Dexter" ORDER BY genres.name;
