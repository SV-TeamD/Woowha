import os
import json
import time
import logging
from flask.json import jsonify

import imagehash

ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(",")
INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")
WAIT_FOR_OUTPUT_IMAGE_SECOND = os.getenv("WAIT_FOR_OUTPUT_IMAGE_SECOND")
STYLES = os.getenv("STYLES").split(",")
STYLES_BACKUP = os.getenv("STYLES_BACKUP").split(",")


class _Utils:
    LOGGER = logging.getLogger(__name__)

    @classmethod
    def _file_extension(cls, filename):
        if not "." in filename:
            return None
        return filename.split(".")[1].lower()

    @classmethod
    def _fileid_from_image(cls, img):
        return str(imagehash.phash(img))

    @classmethod
    def exist_file(cls, filepath):
        return os.path.exists(filepath)

    @classmethod
    def file_from_storage(cls, path):
        filenames = os.listdir(path)
        files = []
        for filename in filenames:
            ext = cls._file_extension(filename)
            if ext in ALLOWED_EXTENSIONS:
                files.append(filename)
        return files

    @classmethod
    def filename_and_style(cls, output_filename: str):
        """
        return: [filename, style]
        """
        [filename, extension] = output_filename.split(".")
        [filename, style] = filename.split("_", 1)
        return [".".join([filename, extension]), style]

    @classmethod
    def input_filename(cls, img, filename):
        fileid = cls._fileid_from_image(img)
        extension = cls._file_extension(filename)
        return ".".join([fileid, extension])

    @classmethod
    def job_message(cls, filename, style):
        return json.dumps({"filename": filename, "style": style})

    @classmethod
    def output_filename(cls, input_filename: str, style: str):
        filename_parts = input_filename.split(".")
        return "{}_{}.{}".format(filename_parts[0], style, filename_parts[1])


    @classmethod
    def response_message(cls, input_filename):
        return jsonify({"filename": input_filename})

    @classmethod
    def wait_until_save_image(cls, img, input_filename):
        """storage에 이미지를 저장하고 완료될 때까지 기다린다.

        Args:
            img (cv2.Image): 저장할 이미지
            input_filename (str): 저장할 이미지의 파일 이름
        """
        save_path = os.path.join(INPUT_FOLDER, input_filename)
        img.save(save_path)
        cls.LOGGER.debug("Image saving.")
        while not cls.exist_file(save_path): # 파일이 존재할 때까지 반복
            time.sleep(0.5)
            cls.LOGGER.debug("Image doesn't saved yet.")

        if cls.exist_file(save_path):
            cls.LOGGER.debug("Image saving.")
        time.sleep(1.5)


    @classmethod
    def verify_filename_style(cls, filename, style):
        try:
            cls.verify_extension(filename)
            cls.verify_style(style)
            return True
        except Exception as e:
            cls.LOGGER.error(e)
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
        if not style in STYLES and not style in STYLES_BACKUP:
            err_msg = "{} Style not allowed. we can only {}".format(style, STYLES)
            cls.LOGGER.error(err_msg)
            raise ValueError(err_msg)
