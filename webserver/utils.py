import os
import json
import logging
from flask.json import jsonify

import imagehash

ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")
INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")
WAIT_FOR_OUTPUT_IMAGE_SECOND = os.getenv("WAIT_FOR_OUTPUT_IMAGE_SECOND")
STYLES = os.getenv("STYLES")


class _Utils:
    LOGGER = logging.getLogger(__name__)

    @classmethod
    def _file_extension(cls, filename):
        if not "." in filename:
            return None
        return filename.split(".")[1]

    @classmethod
    def _fileid_from_image(cls, img):
        return str(imagehash.phash(img))

    @classmethod
    def verify_file_style(cls, file, style):
        try:
            filename = file.filename
            return cls.verify_filename_style(filename, style)
        except Exception as e:
            return False

    @classmethod
    def verify_filename_style(cls, filename, style):
        try:
            cls.verify_extension(filename)
            cls.verify_style(style)
            return True
        except Exception as e:
            return False

    @classmethod
    def verify_extension(cls, filename):
        if not cls._file_extension(filename) in ALLOWED_EXTENSIONS:
            err_msg = "File extension({}) not allowed. we can only {}".format(
                cls._file_extension(filename), ALLOWED_EXTENSIONS
            )
            cls.LOGGER.error(err_msg)
            raise TypeError(err_msg)

    @classmethod
    def verify_style(cls, style):
        if not style in STYLES:
            err_msg = "{} Style not allowed. we can only {}".format(style, STYLES)
            cls.LOGGER.error(err_msg)
            raise ValueError(err_msg)

    @classmethod
    def output_path(cls, output_filename):
        return os.path.join(OUTPUT_FOLDER, output_filename)

    @classmethod
    def response_message(cls, input_filename):
        return jsonify({"filename": input_filename})

    @classmethod
    def input_filename(cls, img, filename):
        fileid = cls._fileid_from_image(img)
        extension = cls._file_extension(filename)
        return ".".join([fileid, extension])

    @classmethod
    def save_image(cls, img, input_filename):
        img.save(os.path.join(INPUT_FOLDER, input_filename))

    @classmethod
    def job_message(cls, filename, style):
        return json.dumps({"filename": filename, "style": style})
