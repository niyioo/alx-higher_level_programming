#!/usr/bin/python3
"""
A module that defines the City class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class that inherits from Base.
    Represents the cities table in the database.
    """

    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
