from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from send_queue import sendQueue

UPLOAD_FOLDER = "./input_img/"

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f_author = request.form["author"]

        if f and allowed_file(f.filename):
            f_name = request.files["file"].filename
            f_url = UPLOAD_FOLDER + f_author + "_" + f_name
            f.save(f_url)

            send_q = sendQueue()
            send_q.send_url(f_url)

            return "파일 로컬파일에 저장."
        return render_template("test.html")
    return render_template("test.html")