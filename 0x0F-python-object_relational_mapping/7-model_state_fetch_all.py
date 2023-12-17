#!/usr/bin/python3
"""This module provides provides a script that
lists all state objects from a given database.
"""
import sys
from sqlalchemy import create_engine

from model_state import Base, State


if __name__ == "__main__":
    # Create the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session
    session = Session(engine)

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
