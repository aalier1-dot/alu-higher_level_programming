#!/usr/bin/python3
"""Prints State with given name."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    s = session.query(State).filter(State.name == sys.argv[4]).first()
    if s:
        print(s.id)
    else:
        print("Not found")
    session.close()
