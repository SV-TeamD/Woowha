import os
import json

from flask import Blueprint, render_template, request
from werkzeug.utils import redirect
from PIL import Image
import imagehash

from database import db
from database.image_model import ImageModel
from job_producer import JobProducer
from utils import _Utils


INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")

bp = Blueprint("image_route", __name__, url_prefix="/image")
jobProducer = JobProducer()
_utils = _Utils()

# http://locahost:5000/image/upload
@bp.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            print("No file")
            return redirect(request.url)
        file = request.files["file"]
        author = request.form["author"]

        if file and _utils.allowed_file(file.filename):
            img = Image.open(file)
            file_id = str(imagehash.phash(img))
            input_filename = _utils.get_input_filename(file_id)
            img.save(os.path.join(INPUT_FOLDER, input_filename))  # file save in local

            message = {"filename": input_filename, "author": author}
            jobProducer.add_job(message=json.dumps(message))
            print("SEND : {} to {}".format(input_filename, author))

            imagemodel = ImageModel(file_id=file_id, styles=[author])
            db.session.add(imagemodel)
            db.session.commit()
            print("SAVE : {} to {}".format(input_filename, author))

            return str(file_id)

        return render_template("test.html")
    return render_template("test.html")


# http://locahost:5000/image/result/file_id?author=Hayao
@bp.route("/result/<string:file_id>", methods=["GET"])
def result_page(file_id):
    author = request.args.get("author")
    if not author:
        raise Exception("no author in url")

    output_filename = _utils.get_output_filename(file_id, author)
    file_url = os.path.join(OUTPUT_FOLDER, output_filename)
    _utils.is_file_until_yes(file_url)  # polling
    return output_filename, 200
