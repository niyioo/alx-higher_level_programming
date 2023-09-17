#!/usr/bin/python3
"""
A script to list all cities of a specified state from a MySQL database.

Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and lists all cities of the specified state.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./5-cities_by_state.py <username><password> <database> "
              "<state_name>")
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

        # Execute the SQL query to select cities of the specified state
        cursor.execute("SELECT cities.id, cities.name, states.name "
                       "FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = '{}';".format(sys.argv[4])
                       )

        rows = cursor.fetchall()

        # Display the concatenated city names
        print(", ".join([state[1] for state in states]))

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
