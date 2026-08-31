#!/usr/bin/python3
"""Lists all City objects with state names."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    for c, s in session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
