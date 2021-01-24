import logging

from flask import Flask, request

from database import db
from database.cache import Cache
from routes import main_route, image_route
from logs import logger


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    register_extensions(app)
    register_blueprints(app)

    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        api_logger = logging.getLogger("app.api")
        api_logger.info(
            "%s %s %s %s", request.remote_addr, request.method, request.path, response.status
        )
        return response

    return app


def register_extensions(app):
    with app.app_context():
        """Logs"""
        logger.init_app(app)

        """ORM"""
        db.init_app(app)
        # db.drop_all()
        db.create_all()

        """Cache"""
        Cache()


def register_blueprints(app):
    """Blueprints"""
    app.register_blueprint(main_route.bp)
    app.register_blueprint(image_route.bp)


if __name__ == "__main__":
    _app = create_app()
    _app.run(host="0.0.0.0", debug=True)
