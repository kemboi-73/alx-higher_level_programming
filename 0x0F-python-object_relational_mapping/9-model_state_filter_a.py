#!/usr/bin/python3
"""Lists all State objects that contain the letter a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing the letter 'a', sorted by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

