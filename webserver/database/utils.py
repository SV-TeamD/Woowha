class SQLAlchemyDBConnection:
    """SQLAlchemy database connection"""

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.session = self.db.session
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.commit()
        except ConnectionError as connection_error:
            self.session.rollback()
            raise ConnectionError from connection_error
        finally:
            self.session.close()
