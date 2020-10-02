# Challenge: Movies

# Goal: 
-   Write SQL queries to answer questions about a database of movies.

# Language/s: 
-   SQL

# Getting Started:

Here’s how to download this problem into your own CS50 IDE. Log into CS50 IDE and then, in a terminal window, execute each of the below.

Make sure you're in ~/ (i.e., your home directory, aka ~):

``` 
$ cd ~/

```

If you haven’t already, make (i.e., create) a directory called pset7 in your home directory:

```
$ mkdir pset7
```
Change into (i.e., open) that directory:

```
$ cd ~/pset7
```

Now to download a (compressed) ZIP file with this problem’s distribution:

```
wget https://cdn.cs50.net/2019/fall/psets/7/movies/movies.zip

```
Unzip (or uncompress) the movies.zip file: 

```
unzip movies.zip

```
Remove the zipped folder (followed by yes or y to delete that ZIP file.):

```            
$ rm movies.zip
```

Perform ls to check the contents of the current directory:

```
ls
```
You should see a directory called movies (which was inside of that ZIP file). 
Go into this folder:

```
$ cd movies
$ ls
```
    
You should see a movies.db file, and some empty .sql files as well.

Alternatively: you’re welcome to download and unzip:

```
cdn.cs50.net/2019/fall/psets/7/movies/movies.zip 
```

on your own computer and then open it in DB Browser for SQLite. 

NB: Be sure to upload your .sql files to CS50 IDE ultimately 
so that you can submit them via submit50.

# Understanding

Provided to you is a file called movies.db:

A SQLite database that stores data from IMDb about movies, the people who directed and starred in them, and their ratings. 

In a terminal window, run

```
sqlite3 movies.db 
```

so that you can begin executing queries on the database.

First: 

when sqlite3 prompts you to provide a query, type:

```
 .schema
```

and press enter. 

This will output the CREATE TABLE statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.

## The Schema of movies.db:

```
CREATE TABLE movies (
                    id INTEGER,
                    title TEXT NOT NULL,
                    year NUMERIC,
                    PRIMARY KEY(id)
                );
                
CREATE TABLE stars (
                movie_id INTEGER NOT NULL,
                person_id INTEGER NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(person_id) REFERENCES people(id)
            );
            
CREATE TABLE directors (
                movie_id INTEGER NOT NULL,
                person_id INTEGER NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(person_id) REFERENCES people(id)
            );
            
CREATE TABLE ratings (
                movie_id INTEGER NOT NULL,
                rating REAL NOT NULL,
                votes INTEGER NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(id)
            );
            
CREATE TABLE people (
                id INTEGER,
                name TEXT NOT NULL,
                birth NUMERIC,
                PRIMARY KEY(id)
            );
            
CREATE INDEX name_index 
ON people (name);

CREATE INDEX stars_index 
ON stars (person_id);

CREATE INDEX movies_index 
ON movies (year);
```


## Database Tables:

Notice that the movies table has:

*	an id column that uniquely identifies each movie, 
* 	as well as columns for the title of a movie and the year in which the movie was released. 

The people table also has an id column, and also has columns for each person’s name and birth year.

Movie ratings, meanwhile, are stored in the ratings table. The first column in the table is movie_id: a foreign key that references the id of the movies table. The rest of the row contains data about the rating for each movie and the number of votes the movie has received on IMDb.

Finally, the stars and directors tables match people to the movies in which they acted or directed. (Only principal stars and directors are included.) Each table has just two columns: movie_id and person_id, which reference a specific movie and person, respectively.


## Your challenge: 

The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables.

# Specification:

-	For each of the following problems (13 altogether), 
	you should write a single SQL query that outputs the results specified by each problem. 

-   Your response must take the form of a single SQL query, 
    though you may nest other queries inside of your query. 
    
-   You should not assume anything about the ids of any particular movies or people: 
    -   your queries should be accurate even if the id of any particular movie or person were different
-   Finally, each query should return only the data necessary to answer the question: 
    -   if the problem only asks you to output the names of movies, for example, 
        then your query should not also output the each movie’s release year.

You’re welcome to check your queries’ results against IMDb itself, but realize that ratings on the website might differ from those in movies.db, as more votes might have been cast since we downloaded the data!

## TODO:

### In 1.sql:

#### Write a SQL query: 

-   to list the titles of all movies released in 2008.

#### Expected Output: 

-   Your query should output a table with a single column for the title of each movie.

#### Testing:

-   Executing 1.sql results in a table with 1 column and 9,480 rows.

### In 2.sql:   

#### Write a SQL query: 

-   to determine the birth year of Emma Stone.
  
#### Expected Output:

-   Your query should output a table with a single column and a single row (plus optional header)
        containing Emma Stone’s birth year.
        
-   You may assume that there is only one person in the database with the name Emma Stone.

#### Testing:

-	Executing 2.sql results in a table with 1 column and 1 row.


### In 3.sql:   
#### Write a SQL query: 

-	to list the titles of all movies with a release date on or after 2018, 
    in alphabetical order.
    
#### Expected Output:

-   Your query should output a table with a single column for the title of each movie.
 
-   Movies released in 2018 should be included, as should movies with release dates in the future.

#### Testing: 

-	Executing 3.sql results in a table with 1 column and 35,755 rows.


### In 4.sql:   
#### Write a SQL query:

-	to determine the number of movies with an IMDb rating of 10.0.

#### Expected Output:

-   Your query should output a table with a single column and a single row (plus optional header) containing the number of movies with a 10.0 rating.

#### Testing:

-	Executing 4.sql results in a table with 1 column and 1 row.

### In 5.sql:
#### Write a SQL query:

-	to list the titles and release years of all Harry Potter movies, in chronological order.

#### Expected Output:

-   Your query should output a table with two columns:
        
    -   one for the title of each movie
    
    -   &N one for the release year of each movie.
    
-   You may assume that: 

	-	the title of all Harry Potter movies will begin with the words “Harry Potter”,
	
   -	if a movie title begins with the words “Harry Potter”, it is a Harry Potter movie.
        
#### Testing:

-	Executing 5.sql results in a table with 2 columns and 10 rows.      
        
### In 6.sql:   
#### Write a SQL query: 

-	to determine the average rating of all movies released in 2012.

#### Expected Output:

-	Your query should output a table with a single column and a single row (plus optional header) containing the average rating.

#### Testing:

-	Executing 6.sql results in a table with 1 column and 1 row.


### In 7.sql:   
#### Write a SQL query

-	to list all movies released in 2010 and their ratings, in descending order by rating. 

#### Expected Output:

-   For movies with the same rating, order them alphabetically by title.

-   Your query should output a table with two columns: 

    -   one for the title of each movie
    
    -   & one for the rating of each movie.

-   Movies that do not have ratings should not be included in the result.

#### Testing:

-	Executing 7.sql results in a table with 2 columns and 6,835 rows.


### In 8.sql:   
#### Write a SQL query:
 
-	to list the names of all people who starred in Toy Story.

#### Expected Output:

-	Your query should output a table with a single column for the name of each person.

-	You may assume that there is only one movie in the database with the title Toy Story.

#### Testing: 

-	Executing 8.sql results in a table with 1 column and 4 rows.


### In 9.sql:
#### Write a SQL query:

-	to list the names of all people who starred in a movie released in 2004, ordered by birth year.

#### Expected Output:

-	Your query should output a table with a single column for the name of each person.

-	People with the same birth year may be listed in any order. No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.

-	If a person appeared in more than one movie in 2004, they should only appear in your results once.


#### Testing:

-	Executing 9.sql results in a table with 1 column and 18,013 rows.


### In 10.sql: 
#### Write a SQL query: 

-	to list the names of all people who have directed a movie that received a rating of at least 9.0.

#### Expected Output:

-	Your query should output a table with a single column for the name of each person.

#### Testing: 

-	Executing 10.sql results in a table with 1 column and 1,841 rows.

### In 11.sql: 
#### Write a SQL query: 

-	to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.

#### Expected Output:

-	Your query should output a table with a single column for the title of each movie.

-	You may assume that there is only one person in the database with the name Chadwick Boseman.

#### Testing:

-	Executing 11.sql results in a table with 1 column and 5 rows.

### In 12.sql: 
#### Write a SQL query: 

-	to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.

#### Expected Output:

-	Your query should output a table with a single column for the title of each movie.

-	You may assume that there is only one person in the database with the name Johnny Depp.

-	You may assume that there is only one person in the database with the name Helena Bonham Carter.

#### Testing:

-	Executing 12.sql results in a table with 1 column and 6 rows.

### In 13.sql: 
#### Write a SQL query: 

-	to list the names of all people who starred in a movie in which Kevin Bacon also starred.

#### Expected Output:

Your query should output a table with a single column for the name of each person.
There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.

#### Testing:

-	Executing 13.sql results in a table with 1 column and 176 rows.


## Usage:

To test your queries on CS50 IDE, you can query the database by running

```
$ cat filename.sql | sqlite3 movies.db

```

(Where filename.sql is the file containing your SQL query.)

Or you can paste them into DB Browser for SQLite’s Execute SQL tab and click ▶.

## Hints:   

See this SQL keywords reference for some SQL syntax that may be helpful!

```
https://www.w3schools.com/sql/sql_ref_keywords.asp

```

## Testing: 

No check50 for this problem! But be sure to test each query and ensure that the output is what you expect. You can run 

```
sqlite3 movies.db 

```

to run additional queries on the database to ensure that your result is correct.

If you’re using the movies.db database provided in this problem set’s distribution, you should find that

```
Executing 1.sql results in a table with 1 column and 9,480 rows.

Executing 2.sql results in a table with 1 column and 1 row.

Executing 3.sql results in a table with 1 column and 35,755 rows.

Executing 4.sql results in a table with 1 column and 1 row.

Executing 5.sql results in a table with 2 columns and 10 rows.

Executing 6.sql results in a table with 1 column and 1 row.

Executing 7.sql results in a table with 2 columns and 6,835 rows.

Executing 8.sql results in a table with 1 column and 4 rows.

Executing 9.sql results in a table with 1 column and 18,013 rows.

Executing 10.sql results in a table with 1 column and 1,841 rows.

Executing 11.sql results in a table with 1 column and 5 rows.

Executing 12.sql results in a table with 1 column and 6 rows.

Executing 13.sql results in a table with 1 column and 176 rows.
```