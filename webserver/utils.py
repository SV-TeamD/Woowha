import os
import time
import json

import imagehash

ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")
INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")
WAIT_FOR_OUTPUT_IMAGE_SECOND = os.getenv("WAIT_FOR_OUTPUT_IMAGE_SECOND")


class _Utils:
    @classmethod
    def allowed_file(cls, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    @classmethod
    def is_file_until_yes(cls, output_filename):
        path = os.path.join(OUTPUT_FOLDER, output_filename)
        while not cls._exist_file(path):
            print("please wait for second...")
            time.sleep(1)

    @classmethod
    def _exist_file(cls, path):
        return os.path.isfile(path)

    @classmethod
    def get_file_id(cls, img):
        return str(imagehash.phash(img))

    @classmethod
    def get_input_filename(cls, file_id):
        cls.file_id = file_id
        cls.input_filename = "{}.jpg".format(file_id)
        return cls.input_filename

    @classmethod
    def get_output_filename(cls, file_id, style):
        cls.output_filename = "{}_{}.jpg".format(file_id, style)
        return cls.output_filename

    @classmethod
    def save_image(cls, img, input_filename=None, file_id=None):
        if input_filename:
            img.save(os.path.join(INPUT_FOLDER, input_filename))
        elif file_id:
            img.save(os.path.join(INPUT_FOLDER, cls.get_input_filename(file_id)))

    @classmethod
    def get_job_message(cls, file_id, style):
        return json.dumps({"file_id": file_id, "style": style})
