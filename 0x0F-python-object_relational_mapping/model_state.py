#!/usr/bin/python3
"""Define the State class and link it to the MySQL table 'states'."""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State class with attributes id and name, linked to 'states' table."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create a connection to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )
    )

    # Create the 'states' table
    Base.metadata.create_all(engine)
