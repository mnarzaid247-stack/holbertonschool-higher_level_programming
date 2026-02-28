#!/usr/bin/python3
"""lists cities"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
    session =Session()
    for city, state in (
            session.query(City, State).join(State).order_by(City.id)
            .all()
            ):
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    main()
