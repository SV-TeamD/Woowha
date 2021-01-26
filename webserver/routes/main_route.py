from flask import Blueprint

from metrics import metrics

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
@metrics.common_counter
def index():
    return "Flask in a Docker!!! Hello World!"
