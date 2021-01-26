import logging

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import redirect
from PIL import Image

from database.cache import Cache
from job_producer import JobProducer
from metrics import metrics
from utils import _Utils

LOGGER = logging.getLogger(current_app)

bp = Blueprint("image_route", __name__, url_prefix="/image")
jobProducer = JobProducer()

# http://locahost:5000/image/upload
@bp.route("/upload", methods=["POST"])
@metrics.common_counter
def upload_file():
    """upload file route

    Returns:
        json: { "filename": input_filename }
    """
    if "file" not in request.files:
        LOGGER.error("No file in request")
        return redirect(request.url)
    if "author" not in request.form:
        LOGGER.error("No style in request")
        return redirect(request.url)

    file = request.files["file"]
    style = request.form["author"]

    if not _Utils.verify_file_style(file, style):
        LOGGER.error("Fail verifing file. Redirect %s", request.url)
        return redirect(request.url)

    img = Image.open(file)
    filename = str(file.filename)
    input_filename = _Utils.input_filename(img, filename)

    if Cache.exist_output_image(input_filename, style):
        return _Utils.response_message(input_filename)
    if not Cache.exist_image(input_filename):
        _Utils.save_image(img, input_filename)

    jobProducer.publish(msg=_Utils.job_message(input_filename, style))
    return _Utils.response_message(input_filename)


# http://locahost:5000/image/result/filename?style=Hayao
@bp.route("/result/<string:filename>", methods=["GET"])
@metrics.common_counter
def result_page(filename: str):
    """result page

    Args:
        filename (str): filename

    Returns:
        json: { "url": url of result image }
    """
    style = request.args.get("style")
    if not _Utils.verify_filename_style(filename, style):
        return "Fail", 500

    try:
        Cache.wait_for_image(filename, style)
        return jsonify({"url": _Utils.output_path(filename)})
    except TimeoutError:
        return "Time out Error", 500
    except Exception:
        return "Fail", 500
