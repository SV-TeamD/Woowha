import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)


class SQLAlchemyDBConnection:
    """SQLAlchemy database connection"""

    def __init__(self):
        self.session = None

    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.commit()
        except ConnectionError as connection_error:
            self.session.rollback()
            raise ConnectionError from connection_error
        finally:
            self.session.close()
