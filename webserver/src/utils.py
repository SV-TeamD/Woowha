import os
import time

ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


class _Utils:
    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    def is_file_until_yes(self, path):
        while not self._exist_file(path):
            print("please wait for second...")
            time.sleep(1)

    def _exist_file(self, path):
        return os.path.isfile(path)
