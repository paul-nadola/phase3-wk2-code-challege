# import os
# import sys

# sys.path.append(os.getcwd)

# from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
# from sqlalchemy.orm import relationship, backref
# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()

# engine = create_engine('sqlite:///db/concerts.db', echo=True)


# class Band(Base):
#     __tablename__ = 'bands'

#     id = Column(Integer, primary_key=True)
#     name = Column(String())
#     hometown = Column(String())

#     concerts = relationship('Concert', backref= backref('band'))

#     def concerts(self):
#         return [concert for concert in Concert.query if concert.band == self]

#     def venues(self):
#         return [concert.venue for concert in self.concerts()]

#     def play_in_venue(self, venue, date):
#         concert = Concert(date=date, band=self, venue=venue)
#         return concert

#     def all_introductions(self):
#         introductions = []
#         for concert in self.concerts:
#             introduction = f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
#             introductions.append(introduction)
#         return introductions

#     @classmethod
#     def most_performances(cls):
#         bands = cls.query.all()
#         return max(bands, key=lambda band: len(band.concerts))
    
#     def __repr__(self):
#         return f'Band: {self.name}'


# class Venue(Base):
#     __tablename__ = 'venues'

#     id = Column(Integer, primary_key=True)
#     title = Column(String())
#     city = Column(String())

#     concerts = relationship('Concert', backref= backref('venue'))

#     def concerts(self):
#         return [concert for concert in Concert.query if concert.venue == self]

#     def bands(self):
#         return [concert.band for concert in self.concerts()]

#     def concert_on(self, date):
#         for concert in self.concerts:
#             if concert.date == date:
#                 return concert
#         return None

#     def most_frequent_band(self):
#         bands = self.bands()
#         return max(bands, key=lambda band: len(band.concerts))
    
#     def __repr__(self):
#         return f'Venue: {self.title}'


# class Concert(Base):
#     __tablename__ = 'concerts'

#     id = Column(Integer, primary_key=True)
#     date = Column(String())
#     band_id = Column(Integer, ForeignKey('bands.id'))
#     venue_id = Column(Integer, ForeignKey('venues.id'))


#     def __repr__(self):
#         return f'Concert(id={self.id}, Band={self.band_id}, Venue={self.venue_id})'
            
import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///db/concerts.db', echo=True)
Session = sessionmaker(bind=engine)

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())

    concerts = relationship('Concert', backref=backref('band'))

    def concerts(self):
        return [concert for concert in Concert.query if concert.band == self]

    def venues(self):
        return [concert.venue for concert in self.concerts()]

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        return concert    

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        return concert

    def all_introductions(self):
        introductions = []
        for concert in self.concerts:
            introduction = f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            introductions.append(introduction)
        return introductions

    @classmethod
    def most_performances(cls):
        session = Session()
        bands = session.query(cls).all()
        session.close()
        return max(bands, key=lambda band: len(band.concerts))

    def __repr__(self):
        return f'Band: {self.name}'


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())

    concerts = relationship('Concert', backref=backref('venue'))

    def bands(self):
        return [concert.band for concert in self.concerts]

    def concert_on(self, date):
        for concert in self.concerts:
            if concert.date == date:
                return concert
        return None

    def most_frequent_band_id(self):
        bands = self.bands()
        return max(bands, key=lambda band: len(band.concerts)).id

    @classmethod
    def get_band_by_id(cls, band_id):
        session = Session()
        band = session.query(Band).get(band_id)
        session.close()
        return band

    def __repr__(self):
        return f'Venue: {self.title}'


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String())
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    def __repr__(self):
        return f'Concert(id={self.id}, Band={self.band_id}, Venue={self.venue_id})'

