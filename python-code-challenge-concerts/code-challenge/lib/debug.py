#!/usr/bin/env python3
from models import Band, Venue, Concert
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb;


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///db/concerts.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()
