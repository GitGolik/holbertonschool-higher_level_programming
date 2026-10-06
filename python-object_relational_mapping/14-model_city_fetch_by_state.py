#!/usr/bin/python3
"""List all cities with their corresponding states."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(
        State,
        City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(
            state.name,
            city.id,
            city.name
        ))

    session.close()
