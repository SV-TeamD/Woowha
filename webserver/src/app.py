from flask import Flask
from routes import main_route, image_route


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_route.bp)
    app.register_blueprint(image_route.bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
