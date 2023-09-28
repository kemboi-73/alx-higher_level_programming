#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    """
    Function DOC
    """
    db_user, db_password, db_db = argv[1:4]
    db_host = "localhost"

    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_password}@{db_host}/{db_db}', pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use a single query to delete states containing 'a'
    session.query(State).filter(State.name.contains('a')).delete(synchronize_session=False)
    
    session.commit()
    session.close()

if __name__ == "__main__":
    main()

