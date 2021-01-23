from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import redirect
from PIL import Image

from database.cache import Cache
from job_producer import JobProducer
from utils import _Utils

bp = Blueprint("image_route", __name__, url_prefix="/image")
jobProducer = JobProducer()

# http://locahost:5000/image/upload
@bp.route("/upload", methods=["POST"])
def upload_file():
    """upload file route

    Returns:
        str: fileid
    """
    if "file" not in request.files:
        print("No file")
        return redirect(request.url)
    file = request.files["file"]
    style = str(request.form["style"])

    if not file or not _Utils.allowed_file(file.filename):
        return render_template("test.html")

    img = Image.open(file)
    filename = str(file.filename)
    input_filename = _Utils.get_input_filename(img, filename)

    if Cache.exist_output_image(input_filename, style):
        print("exist output image in cache")
        return str(input_filename)
    if not Cache.exist_image(input_filename):
        print("no image in cache")
        _Utils.save_image(img, input_filename)

    jobProducer.add_job(message=_Utils.get_job_message(input_filename, style))
    print("SEND : {} to {}".format(input_filename, style))

    return _Utils.get_fileid_from_filename(input_filename)


# http://locahost:5000/image/result/fileid?style=Hayao
@bp.route("/result/<string:fileid>", methods=["GET"])
def result_page(fileid: str):
    """result page

    Args:
        fileid (str): fileid

    Returns:
        json: { "url": url of result image }
    """
    style = request.args.get("style")
    if not style:
        raise Exception("no style in url")

    try:
        Cache.wait_for_image(fileid, style)

        return "success", 200
        # return jsonify({'url': })
    except TimeoutError:
        return "faile", 500
