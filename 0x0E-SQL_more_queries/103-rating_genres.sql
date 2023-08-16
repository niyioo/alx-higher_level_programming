-- List genres and their rating sum, sorted by descending rating
SELECT tv_genres.name, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY rating_sum DESC;
