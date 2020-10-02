Challenge: Houses

CONTENTS:
-   Languages                               14
-   Goal                                    17
-   Required Command-line Arguments         20
-   Getting Started                         24
-   Background                              40
-   Specification                           46
    -   import.py                           48
    -   roster.py                           89
-   Importing CS50 & SQL                    123

*** Languages: ***
    SQL, SQLite3, Python3

*** Goal: ***
    Implement a program to import student data into a database, and then produce class rosters.

*** Required Command-line Arguments: ***
    $ python import.py characters.csv
    $ python roster.py Gryffindor

*** Getting Started ***

Here’s how to download this problem into your own CS50 IDE. Log into CS50 IDE and then, in a terminal window, execute each of the below.

-   Execute cd to ensure that you’re in ~/ (i.e., your home directory, aka ~).
-   If you haven’t already, 
        execute mkdir pset7 to make (i.e., create) a directory called pset7 in your home directory.
-   Execute cd pset7 to change into (i.e., open) that directory.
-   Execute wget https://cdn.cs50.net/2019/fall/psets/7/houses/houses.zip 
    to download a (compressed) ZIP -  file with this problem’s distribution.
-   Execute unzip houses.zip to uncompress that file.
-   Execute rm houses.zip followed by yes or y to delete that ZIP file.
-   Execute ls. You should see a directory called houses, which was inside of that ZIP file.
-   Execute cd houses to change into that directory.
-   Execute ls. You should see a characters.csv file and a students.db database.

*** Background ***

Hogwarts is in need of a student database. For years, the professors have been maintaing a CSV file containing all of the students’ names and houses and years. But that file didn’t make it particularly easy to get access to certain data, such as a roster of all the Ravenclaw students, or an alphabetical listing of the students enrolled at the school.

The challenge ahead of you is to import all of the school’s data into a SQLite database, and write a Python program to query that database to get house rosters for each of the houses of Hogwarts.

*** Specification ***

* In import.py, * 
-   Goal: 
        write a program that imports data from a CSV spreadsheet.

-   You may assume: 
    -   the CSV file:
        -   will exist, 
        -   will have columns: name, house, and birth.
        -   each person’s name field will contain either 
            ->  two space-separated names (a first and last name)
            OR three space-separated names (a first, middle, and last name). 

    -   The database has separate columns for first, middle, and last names. 

-   Requirements: 
    -   Your program should accept the name of a CSV file as a command-line argument.
    -   If the incorrect number of command-line arguments are provided, 
        your program should print an error and exit.

    -   For each student in the CSV file, 
        ->  insert the student into the students table in the students.db database.

    -   You’ll thus want to first parse each name
        & separate it into first, middle, and last names. 

    -   For students without a middle name, 
        -   you should leave their middle name field as NULL in the table.

-   Expected Output:
    -   Your code should import the all the information from CSV file to the database. 

-   Querying the data in the database:
    -   To check that you've been successful:
            sqlite3 students.db
            # Print the lines in the database:
            SELECT * FROM students; 
    -   To delete the info in the database (if you didn't successfully import all the information):
            DELETE FROM students;
    -   There should be 40 lines for the 40 students in the database:
            SELECT COUNT(*) FROM students;

* In roster.py: *
-   * Goal: 
        write a program that prints a list of students for a given house in alphabetical order.

-   * Requirements:
    -   Your program should accept the name of a house as a command-line argument.
    -   If the incorrect number of command-line arguments are provided, 
        your program should print an error and exit.
    -   Your program should query the students table in the students.db database 
        for all of the students in the specified house.
    -   Your program should then print out each student’s full name and birth year 
        (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
    -   Each student should be printed on their own line.
    -   Students should be ordered by last name. 
        ->  For students with the same last name, they should be ordered by first name.

    * Expected Output:

    When you run: 
        $ python roster.py Gryffindor
    You should get the following output:

Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980

*** Importing CS50 & SQL: ***
-   pip install cs50

