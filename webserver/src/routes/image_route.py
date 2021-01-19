import os
import time
import json

from flask import Blueprint, render_template, request
from werkzeug.utils import redirect, secure_filename

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
        file_author = request.form["author"]

        if file and _utils.allowed_file(file.filename):
            filename = secure_filename(request.files["file"].filename)
            file_url = os.path.join(INPUT_FOLDER, filename)
            f.save(file_url)  # file save in local

            message = {"filename": filename, "author": file_author}
            jobProducer.add_job(message=json.dumps(message))
            print("SEND : {}_{}".format(file_author, filename))
            return "파일 로컬파일에 저장."

        return render_template("test.html")
    return render_template("test.html")


# http://locahost:5000/image/result/filename?author=Hayao
@bp.route("/result/<string:filename>", methods=["GET"])
def result_page(filename):
    author = request.args.get("author")
    if not author:
        raise Exception("no author in url")

    output_filename = "{}_{}".format(author, filename)
    file_url = os.path.join(OUTPUT_FOLDER, output_filename)
    _utils.is_file_until_yes(file_url)  # polling
    return output_filename, 200
