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
    def get_file_extension(cls, filename):
        return filename.split(".")[1]

    @classmethod
    def allowed_file(cls, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    @classmethod
    def get_output_path(cls, output_filename):
        path = os.path.join(OUTPUT_FOLDER, output_filename)

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
    def get_fileid_from_image(cls, img):
        return str(imagehash.phash(img))

    @classmethod
    def get_fileid_from_filename(cls, filename: str):
        return str(filename).split(".")[0]

    @classmethod
    def get_input_filename(cls, img, filename):
        fileid = cls.get_fileid_from_image(img)
        extension = cls.get_file_extension(filename)
        return ".".join([fileid, extension])

    @classmethod
    def save_image(cls, img, input_filename):
        img.save(os.path.join(INPUT_FOLDER, input_filename))

    @classmethod
    def get_job_message(cls, filename, style):
        return json.dumps({"filename": filename, "style": style})
