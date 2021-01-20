from flask import Flask

from database import db
from routes import main_route, image_route


def create_app():
    _app = Flask(__name__)
    _app.config.from_object("config")

    # ORM
    db.init_app(_app)

    # blueprint
    _app.register_blueprint(main_route.bp)
    _app.register_blueprint(image_route.bp)

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
