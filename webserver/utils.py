import os
import time

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


class _Utils:
    @classmethod
    def allowed_file(cls, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    @classmethod
    def is_file_until_yes(cls, path):
        while not cls._exist_file(path):
            print("please wait for second...")
            time.sleep(1)

    @classmethod
    def _exist_file(cls, path):
        return os.path.isfile(path)

    @classmethod
    def get_input_filename(cls, file_id):
        cls.file_id = file_id
        cls.input_filename = "{}.jpg".format(file_id)
        return cls.input_filename

    @classmethod
    def get_output_filename(cls, file_id, author):
        cls.output_filename = "{}_{}.jpg".format(file_id, author)
        return cls.output_filename
