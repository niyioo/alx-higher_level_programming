#!/usr/bin/python3
"""
A script to list states with names starting with 'N' from a MySQL database.

Usage: ./1-filter_states.py <username> <password> <database>
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists states
    with names starting with 'N'.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <database>")
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

        # Execute the SQL query to select states with names
        # starting with 'N' and order by states.id
        cursor.execute(
            "SELECT * FROM states "
            "WHERE CONVERT('name' USING Latin1) "
            "COLLATE Latin1_General_CS "
            "LIKE 'N%' "
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
