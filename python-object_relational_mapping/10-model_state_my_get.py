#!/usr/bin/python3
"""lists with name"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(username, password, database),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (
        session.query(State).filter(State.name == name)
        .order_by(State.id).first()
    )
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()


if __name__ == "__main__":
    main()
