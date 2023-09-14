#!/usr/bin/python3
"""
A script to list all State objects containing the
letter 'a' from a MySQL database.

Usage: ./9-model_state_filter_a.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to a MySQL database and lists State objects containing 'a'.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <username> "
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

        # Query State objects containing 'a' and sort them by ID
        states_with_a = session.query(State)\
            .filter(State.name.like('%a%'))\
            .order_by(State.id)\
            .all()

        # Display the results
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
