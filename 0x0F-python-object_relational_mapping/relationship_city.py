#!/usr/bin/python3
"""
A module that defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base.
    Represents the cities table in the database.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
