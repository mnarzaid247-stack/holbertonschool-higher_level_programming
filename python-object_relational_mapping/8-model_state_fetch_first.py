#!/usr/bin/python3
"""lists the first"""

import sys
from model_state import Base, State
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
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    main()
