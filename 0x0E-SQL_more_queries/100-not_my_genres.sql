-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- run this first to import a SQL dump -->
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--
-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

--The tv_shows table contains only one record where title = Dexter (but the id can be different)
--Each record should display: tv_genres.name
--Results must be sorted in ascending order by the genre name
--You can use a maximum of two SELECT statement

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (SELECT tv_genres.name
FROM tv_genres INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = 'Dexter')
GROUP BY tv_genres.name
ORDER BY tv_genres.name
