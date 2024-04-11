#!/usr/bin/python3
"""
class definition of a City: Inherits from Base
links to the MySQL table cities
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class City; instance of Base
    Linked to MySQL table "city"
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)  # autoincrements
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
