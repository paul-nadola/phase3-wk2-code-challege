import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Band, Venue, Concert

@pytest.fixture
def session():
    engine = create_engine('sqlite:///db/concerts.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# def test_band_concerts(session):
#     band = Band(name='Band1', hometown='City1')
#     session.add(band)
#     session.commit()

#     concert1 = Concert(date='2023-05-27', band=band)
#     concert2 = Concert(date='2023-05-28', band=band)
#     session.add(concert1)
#     session.add(concert2)
#     session.commit()

#     assert len(band.concerts) == 2

# def test_band_venues(session):
#     band = Band(name='Band2', hometown='City2')
#     session.add(band)
#     session.commit()

#     venue1 = Venue(title='Venue1', city='City1')
#     venue2 = Venue(title='Venue2', city='City2')
#     session.add(venue1)
#     session.add(venue2)
#     session.commit()

#     concert1 = Concert(date='2023-05-27', band=band, venue=venue1)
#     concert2 = Concert(date='2023-05-28', band=band, venue=venue2)
#     session.add(concert1)
#     session.add(concert2)
#     session.commit()

#     assert len(band.venues()) == 2

# def test_band_play_in_venue(session):
#     band = Band(name='Band3', hometown='City3')
#     session.add(band)
#     session.commit()

#     venue = Venue(title='Venue3', city='City3')
#     session.add(venue)
#     session.commit()

#     concert = band.play_in_venue(venue=venue, date='2023-05-27')
#     session.add(concert)
#     session.commit()

#     assert concert.band == band
#     assert concert.venue == venue
#     assert concert.date == '2023-05-27'

# def test_band_all_introductions(session):
#     band = Band(name='Band4', hometown='City4')
#     session.add(band)
#     session.commit()

#     venue = Venue(title='Venue4', city='City4')
#     session.add(venue)
#     session.commit()

#     concert = Concert(date='2023-05-27', band=band, venue=venue)
#     session.add(concert)
#     session.commit()

#     introductions = band.all_introductions()

#     assert len(introductions) == 1
#     assert introductions[0] == "Hello City4!!!!! We are Band4 and we're from City4"

# def test_band_most_performances(session):
#     band1 = Band(name='Band5', hometown='City5')
#     band2 = Band(name='Band6', hometown='City6')
#     session.add(band1)
#     session.add(band2)
#     session.commit()

#     venue = Venue(title='Venue5', city='City5')
#     session.add(venue)
#     session.commit()

#     concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
#     concert2 = Concert(date='2023-05-28', band=band1, venue=venue)
#     concert3 = Concert(date='2023-05-29', band=band2, venue=venue)
#     session.add(concert1)
#     session.add(concert2)
#     session.add(concert3)
#     session.commit()

#     most_performed_band = Band.most_performances()

#     assert most_performed_band == band1

# def test_venue_concerts(session):
#     venue = Venue(title='Venue6', city='City6')
#     session.add(venue)
#     session.commit()

#     band1 = Band(name='Band7', hometown='City7')
#     band2 = Band(name='Band8', hometown='City8')
#     session.add(band1)
#     session.add(band2)
#     session.commit()

#     concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
#     concert2 = Concert(date='2023-05-28', band=band2, venue=venue)
#     session.add(concert1)
#     session.add(concert2)
#     session.commit()

#     assert len(venue.concerts()) == 2

# def test_venue_bands(session):
#     venue = Venue(title='Venue7', city='City7')
#     session.add(venue)
#     session.commit()

#     band1 = Band(name='Band9', hometown='City9')
#     band2 = Band(name='Band10', hometown='City10')
#     session.add(band1)
#     session.add(band2)
#     session.commit()

#     concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
#     concert2 = Concert(date='2023-05-28', band=band2, venue=venue)
#     session.add(concert1)
#     session.add(concert2)
#     session.commit()

#     assert len(venue.bands()) == 2

# def test_venue_concert_on(session):
#     venue = Venue(title='Venue8', city='City8')
#     session.add(venue)
#     session.commit()

#     band = Band(name='Band11', hometown='City11')
#     session.add(band)
#     session.commit()

#     concert = Concert(date='2023-05-27', band=band, venue=venue)
#     session.add(concert)
#     session.commit()

#     concert_on_date = venue.concert_on('2023-05-27')

#     assert concert_on_date == concert

# def test_venue_most_frequent_band(session):
#     venue = Venue(title='Venue9', city='City9')
#     session.add(venue)
#     session.commit()

#     band1 = Band(name='Band12', hometown='City12')
#     band2 = Band(name='Band13', hometown='City13')
#     session.add(band1)
#     session.add(band2)
#     session.commit()

#     concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
#     concert2 = Concert(date='2023-05-28', band=band1, venue=venue)
#     concert3 = Concert(date='2023-05-29', band=band2, venue=venue)
#     session.add(concert1)
#     session.add(concert2)
#     session.add(concert3)
#     session.commit()

#     most_frequent_band = venue.most_frequent_band()

#     assert most_frequent_band == band1

def test_band_play_in_venue(session):
    venue = Venue(title='Venue1', city='City1')
    session.add(venue)
    session.commit()

    band = Band(name='Band1', hometown='City1')
    session.add(band)
    session.commit()

    concert = band.play_in_venue(venue, date='2023-05-26')

    assert concert.band == band
    assert concert.venue == venue

def test_band_all_introductions(session):
    venue = Venue(title='Venue2', city='City2')
    session.add(venue)
    session.commit()

    band = Band(name='Band2', hometown='City2')
    session.add(band)
    session.commit()

    concert1 = Concert(date='2023-05-27', band=band, venue=venue)
    concert2 = Concert(date='2023-05-28', band=band, venue=venue)
    session.add(concert1)
    session.add(concert2)
    session.commit()

    introductions = band.all_introductions()

    assert len(introductions) == 2
    assert introductions[0] == "Hello City2!!!!! We are Band2 and we're from City2"
    assert introductions[1] == "Hello City2!!!!! We are Band2 and we're from City2"

def test_band_most_performances(session):
    venue = Venue(title='Venue3', city='City3')
    session.add(venue)
    session.commit()

    band1 = Band(name='Band3', hometown='City3')
    band2 = Band(name='Band4', hometown='City4')
    session.add(band1)
    session.add(band2)
    session.commit()

    concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
    concert2 = Concert(date='2023-05-28', band=band1, venue=venue)
    concert3 = Concert(date='2023-05-29', band=band2, venue=venue)
    session.add(concert1)
    session.add(concert2)
    session.add(concert3)
    session.commit()

    most_performed_band = Band.most_performances()

    assert most_performed_band.id == band1.id

def test_venue_bands(session):
    venue = Venue(title='Venue4', city='City4')
    session.add(venue)
    session.commit()

    band1 = Band(name='Band5', hometown='City5')
    band2 = Band(name='Band6', hometown='City6')
    session.add(band1)
    session.add(band2)
    session.commit()

    concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
    concert2 = Concert(date='2023-05-28', band=band2, venue=venue)
    session.add(concert1)
    session.add(concert2)
    session.commit()

    bands = venue.bands()

    assert len(bands) == 2
    assert band1 in bands
    assert band2 in bands

def test_venue_concert_on(session):
    venue = Venue(title='Venue5', city='City5')
    session.add(venue)
    session.commit()

    band = Band(name='Band7', hometown='City7')
    session.add(band)
    session.commit()

    concert1 = Concert(date='2023-05-27', band=band, venue=venue)
    concert2 = Concert(date='2023-05-28', band=band, venue=venue)
    session.add(concert1)
    session.add(concert2)
    session.commit()

    concert = venue.concert_on(date='2023-05-28')

    assert concert.band == band
    assert concert.venue == venue

def test_venue_most_frequent_band_id(session):
    venue = Venue(title='Venue6', city='City6')
    session.add(venue)
    session.commit()

    band1 = Band(name='Band8', hometown='City8')
    band2 = Band(name='Band9', hometown='City9')
    session.add(band1)
    session.add(band2)
    session.commit()

    concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
    concert2 = Concert(date='2023-05-28', band=band1, venue=venue)
    concert3 = Concert(date='2023-05-29', band=band2, venue=venue)
    session.add(concert1)
    session.add(concert2)
    session.add(concert3)
    session.commit()

    most_frequent_band_id = venue.most_frequent_band_id()

    assert most_frequent_band_id == band1.id

def test_venue_get_band_by_id(session):
    venue = Venue(title='Venue7', city='City7')
    session.add(venue)
    session.commit()

    band1 = Band(name='Band10', hometown='City10')
    band2 = Band(name='Band11', hometown='City11')
    session.add(band1)
    session.add(band2)
    session.commit()

    concert1 = Concert(date='2023-05-27', band=band1, venue=venue)
    concert2 = Concert(date='2023-05-28', band=band2, venue=venue)
    session.add(concert1)
    session.add(concert2)
    session.commit()

    retrieved_band1 = venue.get_band_by_id(band1.id)
    retrieved_band2 = venue.get_band_by_id(band2.id)

    assert retrieved_band1 == band1
    assert retrieved_band2 == band2

