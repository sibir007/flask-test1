from sqlalchemy import create_engine
from sqlalchemy import inspect, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table



engine = create_engine('sqlite:///social_gamification_db(1).db')

metadata_obj = MetaData(bind=engine)

Base = declarative_base()