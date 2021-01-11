from flask import Flask

from .config import config_by_name
from .router import main_routes


def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    app.register_blueprint(main_routes.bp)

    return app
