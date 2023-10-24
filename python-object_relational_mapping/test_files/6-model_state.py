#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        'mariadb+mariadbconnector://{}:{}@127.0.0.1:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)
    Base.metadata.create_all(engine)
    session.close()
