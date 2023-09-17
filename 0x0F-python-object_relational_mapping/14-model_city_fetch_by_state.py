#!/usr/bin/python3

"""a Python file similar to model_state.py named
model_city.py that contains the class definition of a City"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, data))
    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    my_session = sessionmaker(bind=engine)
    session = my_session

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
