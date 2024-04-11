#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
script should take 3 arguments: mysql username, mysql password and database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # database engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    for instance in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))

    session.close()
