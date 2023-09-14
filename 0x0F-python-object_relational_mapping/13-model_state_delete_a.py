#!/usr/bin/python3
"""
A script to delete State objects with names containing
the letter 'a' from a MySQL database.

Usage: ./13-model_state_delete_a.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to a MySQL database and deletes State
    objects with names containing 'a'.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> "
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

        # Query and delete all State objects with names containing 'a'
        states_to_delete = session.query(State)\
            .filter(State.name.like('%a%'))\
            .all()
        for state in states_to_delete:
            session.delete(state)

        # Commit the changes
        session.commit()

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
