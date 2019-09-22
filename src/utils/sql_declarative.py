import datetime
import os
import sys

from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import Column, ForeignKey, DateTime, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Website(Base):
    __tablename__ = 'Websites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)


class SearchResult(Base):
    __tablename__ = 'SearchResults'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    url = Column(String(500), nullable=False)
    price = Column(Float, nullable=False)
    query = Column(String(500), nullable=False)
    query_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    website_id = Column(Integer, ForeignKey('Websites.id'))
    website = relationship(Website)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine(os.getenv('POSTGRES_DB'), echo=True)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)