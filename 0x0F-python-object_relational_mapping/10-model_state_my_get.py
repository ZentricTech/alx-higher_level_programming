#!/usr/bin/python3
"""
prints the State object with name passed as argument from db hbtn_0e_6_usa
script takes 4 args:username, password, db and state name to search
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # create database engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # python query
    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")

    session.close()
