# models.py

from sqlalchemy import Column, Integer, String
from database.db import Base

# Model for the dictionary table
class Dictionary(Base):
    __tablename__ = 'dictionary'
    id = Column(Integer, primary_key=True)
    en = Column(String, nullable=False, unique=True)
    de = Column(String, nullable=False)
