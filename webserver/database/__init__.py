from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


class Database:
    @classmethod
    def __init__(cls, app):
        # db.create_all()
        db.init_app(app)
        migrate.init_app(app, db)

    @classmethod
    def add(cls, element: db.Model):
        db.session.add(element)
        db.session.commit()
