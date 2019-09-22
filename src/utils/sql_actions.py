import os

from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.sql_declarative import Base, Website, SearchResult


engine = create_engine(os.getenv('POSTGRES_DB'), echo=True)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

maker = sessionmaker(bind=engine)
session = maker()

# Insert a Person in the person table
# objects = [
# 	Website(name='eBay'),
# 	Website(name='Craigslist'),
# 	Website(name='AliExpress'),
# 	Website(name='Walmart'),
# ]
# session.add_all(objects)
# session.commit()


# objects = [
# 	SearchResult(
# 		name='eBay',
# 		url='test.html',
# 		price=56.76,
# 		website_id=1
# 	),
# 	SearchResult(
# 		name='craigst.l/safdf2345',
# 		url='asdfasdf.html',
# 		price=6.764345,
# 		website_id=3
# 	)
# ]
# session.add_all(objects)
# session.commit()