from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base

from models import Base

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

