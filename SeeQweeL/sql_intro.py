"""
Python Documentation
Desc: Data Persistence: Sqlite 3
All right reserved lotus code studios Dec 2022
"""


import sqlite3
import os

# create database connection : with check if the database exists in the current directory

db_filename = "users.db"
db_is_new = not os.path.exists(db_filename)

# loop till the application is exited
while True:
    # check for existing database
    if db_is_new:
        # create a database connection
        conn = sqlite3.connect(db_filename)
        # create a cursor object to execute operations in the database
        cursor = conn.cursor()

        cursor.executescript(
            """
            CREATE TABLE users(
                Name text,
                Phone text,
                Desc text
            );

            """
        )

        conn.commit()
        conn.close()
    else:

        print(
              """
                Welcome to Database X\n
                1. Update Database  [U]\n
                2. Retrieve Records [R]\n
                3. Exit Application [E]
              """
              )

        choice = str(input("Choose Operation: "))

        if choice.casefold() == "u":
            # interface initialization
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            desc = input("Write About Yourself: ")

            # data = [(name, phone, desc)]

            conn = sqlite3.connect(db_filename)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (Name, Phone, Desc) VALUES (?,?,?)", (name, phone, desc))
            conn.commit()
            conn.close()
            print("records updated")

        elif choice.casefold() == "r":
            # retrieving records from the database
            conn = sqlite3.connect(db_filename)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users")
            records = cursor.fetchall()
            print(records)
            conn.commit()
            conn.close()
            pass

        elif choice.casefold() == "e":
            print("Application Exit ...")
            break
        else:
            print("Invalid Operation")






