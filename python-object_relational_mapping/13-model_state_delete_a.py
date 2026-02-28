#!/usr/bin/python3
"""delete"""

import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State


def main():
    """main def"""
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
    state = session.query(State).filter(State.name.like('%a%')).all()
    for n in state:
        session.delete(n)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
