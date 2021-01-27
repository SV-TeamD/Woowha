from flask import Blueprint

from metrics.metrics_register import MetricsRegister

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
@MetricsRegister.common_counter
def index():
    return "Flask in a Docker!!! Hello World!"


@bp.errorhandler(500)
def handle_500(error):
    return str(error), 500
