from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint("model", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return "model server index"


@bp.route("/output_image/<int:index>", methods=["GET"])
def output_image(index):
    return "image index is {}".format(index)
