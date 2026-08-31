#!/usr/bin/python3
"""Lists states containing letter a."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    query = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id)
    for s in query.all():
        print("{}: {}".format(s.id, s.name))
    session.close()
