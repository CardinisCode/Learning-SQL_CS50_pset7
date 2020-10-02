SELECT movies.title
FROM 
	(SELECT stars.movie_id
	FROM stars 
	JOIN people ON stars.person_id = people.id 
	WHERE people.name = "Johnny Depp") 
AS first_person
JOIN 
	(SELECT stars.movie_id
	FROM stars 
	JOIN people ON stars.person_id = people.id 
	WHERE people.name = "Helena Bonham Carter") 
AS second_person ON first_person.movie_id = second_person.movie_id
JOIN movies ON first_person.movie_id = movies.id;