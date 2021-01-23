import logging
from datetime import datetime

from flask import Flask, request

from database import db
from database.cache import Cache
from routes import main_route, image_route
from logs import logger


def create_app():
    _app = Flask(__name__)
    _app.config.from_object("config")

    register_extensions(_app)
    register_blueprints(_app)

    @_app.after_request
    def after_request(response):
        """ Logging after every request. """
        logger = logging.getLogger("app.api")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            datetime.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response

    return _app


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
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
