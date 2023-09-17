#!/usr/bin/python3
"""
A script to retrieve and display states from a MySQL database
based on user input.

Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    Connects to a MySQL database and retrieves states based on user input.
    """
        # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query to select states based on user input
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id ASC".format(argv[4]),
    )

    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)
