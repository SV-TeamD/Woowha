import time

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Flask in a Docker!!! Hello World!"


app.run(host="0.0.0.0", debug=True)
