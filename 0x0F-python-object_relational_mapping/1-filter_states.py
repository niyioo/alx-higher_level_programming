#!/usr/bin/python3
"""
A script to list states with names starting with 'N' from a MySQL database.

Usage: ./1-filter_states.py <username> <password> <database>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to a MySQL database and lists states
    with names starting with 'N'.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY states.id ASC"
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)
