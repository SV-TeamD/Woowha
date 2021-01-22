from typing import List

import redis

from .image_model import ImageModel

cache = redis.Redis(host="redis", port=6379)


class Cache:
    file_list_key = "images:file_list"

    @classmethod
    def add(cls, filename: str, style: str):
        cache.sadd(cls.file_list_key, filename)
        cache.sadd(style, filename)

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
        return bool(cache.sismember(cls.file_list_key, filename))

    @classmethod
    def exist_output_image(cls, filename: str, style: str):
        return bool(cache.sismember(style, filename))
