#!/usr/bin/python3
"""
A script to retrieve and display states from a MySQL database
based on user input.

Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves states based on user input.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Execute the SQL query to select states based on user input
        cursor.execute(
            "SELECT * FROM states "
            "WHERE name = %s "
            "ORDER BY states.id",
            (state_name,)
        )

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
