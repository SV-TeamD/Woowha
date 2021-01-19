from flask import Blueprint

from database.image_model import ImageModel

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return "Flask in a Docker!!! Hello World!"


@bp.route("/test", methods=["GET"])
def test_sql():
    image_id = "0123456789123456"
    image_url = "/data/image_input/jenny.jpg"
    try:
        test = ImageModel(image_id, image_url)

        return "test added. test id={}".format(test.id)
    except Exception as e:
        return str(e)
