from typing import List
import time
import logging

import redis

from .image_model import ImageModel

cache = redis.Redis(host="redis", port=6379)


class Cache:
    file_list_key = "images:file_list"
    LOGGER = logging.getLogger("database.cache")

    @classmethod
    def __init__(cls):
        cls.load_db()

    @classmethod
    def load_db(cls):
        all_data_in_db = ImageModel.query.all()
        if not all_data_in_db:
            return
        cls.add_all_db_data(all_data_in_db)
        cls.LOGGER.debug("Image list: {}".format(cache.smembers(cls.file_list_key)))
        cls.LOGGER.info("Caching image files from DB Done")

    @classmethod
    def add_all_db_data(cls, all_data_in_db: List[ImageModel]):
        all_filename = [x.filename for x in all_data_in_db]
        cache.sadd(cls.file_list_key, *all_filename)
        for image_model in all_data_in_db:
            filename = image_model.filename
            for style in image_model.styles:
                cache.sadd(style, filename)

    @classmethod
    def exist_image(cls, filename: str):
        cls.LOGGER.debug("Image does not exist in cache.")
        cls.LOGGER.debug("Save image")
        return bool(cache.sismember(cls.file_list_key, filename))

    @classmethod
    def exist_output_image(cls, filename: str, style: str):
        cls.LOGGER.debug("Output image exists in cache. Response input filename")
        return bool(cache.sismember(style, filename))

    @classmethod
    def wait_for_image(cls, filename: str, style: str):
        count = 0
        try:
            while count < 10:
                if cls.exist_output_image(filename, style):
                    break
                count += 1
                time.sleep(2)  # 2초마다 실행
        except TimeoutError as timeout_err:
            cls.LOGGER.error("Timeout : %s, %s", filename, style)
            raise TimeoutError from timeout_err
