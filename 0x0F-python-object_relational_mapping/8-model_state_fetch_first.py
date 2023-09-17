#!/usr/bin/python3
"""
A script to print the first State object from a MySQL database.

Usage: ./8-model_state_fetch_first.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to a MySQL database and prints the first State object.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <username> "
              "<password> <database>")
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Create a connection to the MySQL server
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database),
            pool_pre_ping=True
        )

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the first State object and check if it exists
        first_state = session.query(State).first()

        # Display the result or "Nothing" if the table is empty
        if first_state is not None:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
