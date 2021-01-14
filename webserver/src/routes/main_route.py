from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def hello():
    return "Flask in a Docker!!! Hello World!"


@bp.route("/hello")
def hello_pybo():
    return "Hello, Pybo!"
