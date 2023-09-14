#!/usr/bin/python3
"""
A script that prints all City objects from a MySQL database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """
    Connects to a MySQL database and prints all City objects by state.
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> "
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

        # Query all City objects and sort them by city ID
        cities = session.query(City).order_by(City.id).all()

        # Display the results
        for city in cities:
            state = session.query(State).filter_by(id=city.state_id).first()
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
