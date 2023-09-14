#!/usr/bin/python3
"""
A script to print the State object with a
specified name from a MySQL database.

Usage: ./10-model_state_my_get.py <username> <password>
<database> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to a MySQL database and prints the State
    object with the specified name.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Query the State object with the specified name
        state = session.query(State).filter(State.name == state_name).first()

        # Display the result or "Not found" if no state matches the name
        if state is not None:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
