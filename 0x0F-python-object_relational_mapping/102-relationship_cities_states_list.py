#!/usr/bin/python3
"""
A script to list all City objects and their associated State objects
from a MySQL database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def main():
    """
    Connects to a MySQL database and lists City objects with their
    associated State objects.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <username> "
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

        # Query all City objects and their associated State objects
        cities_with_states = session.query(City).order_by(City.id).all()

        # Display the results
        for city in cities_with_states:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
