import os
import time

from flask import Blueprint, url_for, render_template, request
from werkzeug.utils import redirect, secure_filename

from JobProducer import JobProducer
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
            flash("No file")
            return redirect(request.url)
        f = request.files["file"]
        file_author = request.form["author"]

        # TODO: make it to async
        if f and _utils.allowed_file(f.filename):
            filename = secure_filename(request.files["file"].filename)
            file_url = os.path.join(INPUT_FOLDER, "{}_{}".format(file_author, filename))
            f.save(file_url)  # file save in local

            jobProducer.add_job(file_url)
            print("SEND : {}_{}".format(file_author, filename))
            return "파일 로컬파일에 저장."

        return render_template("test.html")
    return render_template("test.html")


# http://locahost:5000/image/result/filename?author=Hayao
@bp.route("/result/<string:filename>", methods=["GET"])
def result_page(filename):
    try:
        author = request.args.get("author")
        output_filename = "{}_{}".format(author, filename)
        file_url = os.path.join(OUTPUT_FOLDER, output_filename)
        _utils.is_file_until_yes(file_url)
        return output_filename, 200
    except expression as e:
        print(e)
        return "ERROR", 500