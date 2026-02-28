#!/usr/bin/python3
"""update"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """the main def"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(username, password, database),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    main()
