#!/usr/bin/python3
"""lists states with a"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """the main function"""
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
    for state in (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    ):
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    main()
