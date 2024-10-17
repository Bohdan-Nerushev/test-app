# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Setting up SQLAlchemy to work with SQLite database
engine = create_engine('sqlite:///database/dictionary.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def get_session():
    """Create a new session."""
    return Session()

# Create the tables if they do not exist
def create_tables():
    Base.metadata.create_all(engine)
