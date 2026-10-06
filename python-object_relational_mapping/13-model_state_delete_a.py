#!/usr/bin/python3
"""delete states whose name contains the letter a"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


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

    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False
    )
    session.commit()

    session.close()
