#!/usr/bin/python3
"""
Defines class State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# instance
Base = declarative_base()


class State(Base):
    """
    Class State; inherits from Base
    links to the MySQL table states
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
