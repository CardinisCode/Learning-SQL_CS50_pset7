SELECT other_stars.name
FROM 
	(SELECT stars.movie_id, people.name, people.birth
	FROM stars 
	JOIN people ON stars.person_id = people.id
	WHERE people.name = "Kevin Bacon" AND people.birth = 1958) 
AS kevin_bacon_1958

JOIN
	(SELECT stars.movie_id, people.name
	FROM stars
	JOIN people ON stars.person_id = people.id
	WHERE people.name IS NOT "Kevin Bacon")
	
AS other_stars
ON kevin_bacon_1958.movie_id = other_stars.movie_id
JOIN movies ON kevin_bacon_1958.movie_id = movies.id
GROUP BY other_stars.name;
