#!/usr/bin/python3
"""
A script to list all State objects and their corresponding City objects
from a MySQL database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main():
    """
    Connects to a MySQL database and lists State and City objects.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <username> "
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

        # Query State objects and their associated City objects
        states_with_cities = session.query(State)\
            .order_by(State.id, City.id)\
            .all()

        # Display the results
        for state in states_with_cities:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
