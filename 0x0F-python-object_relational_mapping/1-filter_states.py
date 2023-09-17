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

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY states.id"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
