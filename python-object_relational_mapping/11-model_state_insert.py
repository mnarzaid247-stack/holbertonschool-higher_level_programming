#!/usr/bin/python3

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
      "mysql+mysqldb://{}:{}
