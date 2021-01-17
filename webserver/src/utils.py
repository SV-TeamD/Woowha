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
