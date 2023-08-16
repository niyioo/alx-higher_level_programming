-- List shows and their rating sum, sorted by descending rating
SELECT tv_shows.title, SUM(tv_shows_rate.rating) AS rating_sum
FROM tv_shows
INNER JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY tv_show_ratings.show_id
ORDER BY rating_sum DESC;
