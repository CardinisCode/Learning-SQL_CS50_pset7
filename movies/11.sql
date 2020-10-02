SELECT movies.title FROM stars
JOIN movies ON  stars.movie_id = movies.id
JOIN ratings ON movies.id = ratings.movie_id
JOIN people ON stars.person_id = people.id
WHERE people.name = "Chadwick Boseman"
ORDER BY rating DESC, movies.year
LIMIT 5;