#!/usr/bin/python3
"""
A script to create the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def main():
    """
    Connects to a MySQL database and creates the State "California"
    with the City "San Francisco".
    """
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <username> "
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

        # Create the State "California" with the City "San Francisco"
        california = State(name="California")
        san_francisco = City(name="San Francisco")
        california.cities.append(san_francisco)

        # Add the State to the session
        session.add(california)

        # Commit the changes to the database
        session.commit()

        # Close the session
        session.close()

        print("State 'California' with City 'San Francisco' "
              "created successfully!")

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
