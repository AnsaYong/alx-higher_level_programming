#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    # Create the connection string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Print the results
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
