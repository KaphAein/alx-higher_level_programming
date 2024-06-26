#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    session.close()
