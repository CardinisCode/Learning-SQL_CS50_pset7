from sys import argv, exit
import csv
import sqlite3
from cs50 import SQL


if len(argv) != 2:
    print("Please provide the name of 1 csv file.")
    exit(1)


hogwarts_school_csv_database = argv[1]
hogwarts_db = SQL("sqlite:///students.db")


def main(hogwarts_school_csv_database, hogwarts_db):
    with open(hogwarts_school_csv_database, newline='') as csvfile:
        c_reader = csv.reader(csvfile)

        names = []
        house = ""
        birth = 0
        last = ""
        student_id = 0

        for row in c_reader:
            print()
            names = row[0].split(' ')
            first = names[0]
            middle = None
            last = ""
            house = row[-2]
            birth = row[-1]

            if first == "name":
                continue

            student_id += 1

            if len(names) == 3:
                middle = names[1]
                last = names[2]
            else:
                last = names[1]

            print(student_id, "|", first, "|", middle, "|", last, "|", house, "|", birth)

            insert_details_into_database(student_id, first, middle, last, house, birth, hogwarts_db)

    exit(0)


def insert_details_into_database(id, first, middle, last, house, birth, hogwarts_db):
    try:
        hogwarts_db.execute('INSERT INTO students VALUES(?, ?, ?, ?, ?, ?)', (id, first, middle, last, house, birth))

    except Exception as error:
        print("", error)


print(main(hogwarts_school_csv_database, hogwarts_db))
