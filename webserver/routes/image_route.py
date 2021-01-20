from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
from PIL import Image

from database import db
from database.image_model import ImageModel
from database.cache import Cache
from job_producer import JobProducer
from utils import _Utils


bp = Blueprint("image_route", __name__, url_prefix="/image")
jobProducer = JobProducer()

# http://locahost:5000/image/upload
@bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        print("No file")
        return redirect(request.url)
    file = request.files["file"]
    author = request.form["author"]

    if not file or not _Utils.allowed_file(file.filename):
        return render_template("test.html")

    img = Image.open(file)
    file_id = _Utils.get_file_id(img)
    input_filename = _Utils.get_input_filename(file_id)

    if Cache.exist_output_image(file_id, author):
        return str(file_id)
    if not Cache.exist_image(file_id):
        _Utils.save_image(img, input_filename, file_id)

    jobProducer.add_job(message=_Utils.get_job_message(input_filename, author))
    print("SEND : {} to {}".format(input_filename, author))

    return str(file_id)


# http://locahost:5000/image/result/file_id?author=Hayao
@bp.route("/result/<string:file_id>", methods=["GET"])
def result_page(file_id):
    author = request.args.get("author")
    if not author:
        raise Exception("no author in url")

    try:
        Cache.wait_for_image_until_10(file_id, author)
        return 200
    except TimeoutError:
        return 500
