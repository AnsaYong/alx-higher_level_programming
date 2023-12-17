#!/usr/bin/python3
"""This module provides provides a script that
lists all state objects from a given database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from model_state import Base, State
from model_state import State


if __name__ == "__main__":
    # Create the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class
    #Base.metadata.bind = engine

    # Create the tables (if they don't exist) based on the models
    #Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id)

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
