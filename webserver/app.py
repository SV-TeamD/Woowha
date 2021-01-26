import logging

from flask import Flask, request

from database import db, migrate
from database.cache import Cache
from logs import logger
from metrics import metrics
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

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
        metrics.init_app(app)

        """ORM"""
        from database import image_model

        db.init_app(app)
        db.create_all()
        migrate.init_app(app, db)
        from database import image_model

        """Cache"""
        Cache()


def register_blueprints(app):
    from routes import main_route, image_route

    """Blueprints"""
    app.register_blueprint(main_route.bp)
    app.register_blueprint(image_route.bp)


if __name__ == "__main__":
    _app = create_app()
    _app.run(host="0.0.0.0", debug=True)
