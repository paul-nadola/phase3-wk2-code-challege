from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Band, Venue, Concert

# Set up the database connection
engine = create_engine('sqlite:///db/concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create an instance of the Faker class
faker = Faker()

# Generate and insert fake data into the database
for _ in range(10):
    # Create a band
    band = Band(
        name=faker.name(),
        hometown=faker.city()
    )
    session.add(band)

    # Create a venue
    venue = Venue(
        title=faker.company(),
        city=faker.city()
    )
    session.add(venue)

    # Create a concert
    concert = Concert(
        date=faker.date(),
        band=band,
        venue=venue
    )
    session.add(concert)

# Commit the changes to the database
session.commit()

# Close the session
session.close()

    
