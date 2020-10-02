from sys import argv, exit
from cs50 import SQL


# We need to make sure that this program will only run if provided with 2 arguments:
# (A Python file name and the name of a valid house)
if len(argv) != 2:
    print("Please provide the name of 1 house.")
    # If not, it will end the program
    exit(1)

house_name = argv[1]
hogwarts_db = SQL("sqlite:///students.db")


# We also need to make sure the user provides the name of a valid house:
if not house_name in ["Ravenclaw", "Slytherin", "Hufflepuff", "Gryffindor"]:
    print(house_name, "is not a valid house name.")
    # If not, it will end the program
    exit(2)


class Student:
    def __init__(self, data, house):
        self.first = data["first"]
        self.middle = None
        if data['middle'] != 'None':
            self.middle = data["middle"]
        self.last = data["last"]
        self.house = house
        self.birth = data["birth"]

    def __str__(self):
        if self.middle == 'None' or self.middle == None:
            self.middle == None
            return "%s %s, born %i" % (self.first, self.last, self.birth)
        else:
            return "%s %s %s, born %i" % (self.first, self.middle, self.last, self.birth)


# The main function will execute the queries:
def main(house_name, hogwarts_db):

    # All queries are executed only if successful
    try:
        # We want to isolate our query to only select & gather the columns we're interestd in:
        # (first, middle, last, birth)
        house_query = """
        SELECT first, middle, last, birth
        FROM students
        WHERE students.house = "%s"
        ORDER BY last, first
        """ % (house_name)

        # Now we can execute this query:
        house_output = hogwarts_db.execute(house_query)

        # Now we have grabbed the relevant details for every student in our database,
        # let's iterate over every student once more, this time we'll string these details together
        # in the format that meets the required criteria:

        for s in house_output:
            student = Student(s, house_name)
            print(student)

        # Now just to end off this current student by printing the formatted string:

    # However, if there should be any errors, they'll be caught and printed here:
    except Exception as error:
        print("asd", error)

    # If all's successful and finished, we can close our program.
    exit(0)


main(house_name, hogwarts_db)
