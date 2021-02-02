import logging

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import redirect
from PIL import Image

from database.cache import Cache
from job_producer import JobProducer

from metrics.metrics_register import MetricsRegister
from utils import _Utils

LOGGER = logging.getLogger(current_app)

bp = Blueprint("image_route", __name__, url_prefix="/image")
jobProducer = JobProducer()

# http://locahost:8000/image/upload
@bp.route("/upload", methods=["POST"])
@MetricsRegister.common_counter
def upload_file():
    """upload file route
    MIMI Type: multipart/form-data

    Args:
        {
            'file', <FileStorage: '03.jpg' ('image/jpeg')>
            "author": "cartoongan_hayao" (exclude extension)
        }

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
    filename = str(file.filename).strip()
    LOGGER.info("file: {}, filename: {}".format(file, filename))

    if not filename:
        return 200
    if not _Utils.verify_filename_style(filename, style):
        LOGGER.error("Fail verifing file. Redirect %s", request.url)
        return redirect(request.url)

    img = Image.open(file)
    input_filename = _Utils.input_filename(img, filename)

    if Cache.exist_output_image(input_filename, style):
        return _Utils.response_message(input_filename)
    if not Cache.exist_image(input_filename):
        _Utils.save_image(img, input_filename) # TODO: 저장하고 보내야 함
    if not Cache.exist_working(input_filename, style):
        Cache.put_working(input_filename, style)
        jobProducer.publish(msg=_Utils.job_message(input_filename, style))

    return _Utils.response_message(input_filename)


# http://locahost:8000/image/result
@bp.route("/result", methods=["POST"])
@MetricsRegister.common_counter
def result_page():
    """result page
    MIMI Type: application/json

    Args:
        {
            "filename": "8bd7299c705c7a2c.jpg", (include extension)
            "style": "cartoongan_hayao" (exclude extension)
        }

    Returns:
        json: { "filename": filename of result image }
    """

    req_data = request.get_json()
    filename = req_data["filename"]
    style = req_data["style"]
    if not _Utils.verify_filename_style(filename, style):
        return "Fail", 500
    try:
        Cache.wait_for_image(filename, style)
        return jsonify({"filename": _Utils.output_filename(filename, style)})
    except TimeoutError as timeout_error:
        LOGGER.error(timeout_error)
        return "Time out Error", 500
    except Exception as e:
        LOGGER.error(e)
        return "Fail", 500
