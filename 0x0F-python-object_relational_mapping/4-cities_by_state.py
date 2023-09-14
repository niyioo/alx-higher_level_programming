#!/usr/bin/python3
"""
A script to list all cities from a MySQL database.

Usage: ./4-cities_by_state.py <username> <password> <database>
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists all cities.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query to select all cities and order by cities.id
        cursor.execute("SELECT * FROM cities ORDER BY cities.id")

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
