-- Lists all Comedy shows in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record
   -- where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title FROM tv_shows AS tv_shows
INNER JOIN tv_show_genres AS shows ON tv_shows.id = shows.show_id

INNER JOIN tv_genres AS genres ON genres.id = shows.genre_id
WHERE genres.name = "Comedy" ORDER BY tv_shows.title;
