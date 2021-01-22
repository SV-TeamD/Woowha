from typing import List

import redis

from .image_model import ImageModel

cache = redis.Redis(host="redis", port=6379)


class Cache:
    file_list_key = "images:file_list"

    @classmethod
    def add(cls, file_id: str, style: str):
        cache.sadd(cls.file_list_key, file_id)
        cache.sadd(style, file_id)

    @classmethod
    def add_all_db_data(cls, all_data_in_db: List[ImageModel]):
        all_file_id = [x.file_id for x in all_data_in_db]
        cache.sadd(cls.file_list_key, *all_file_id)
        for image_model in all_data_in_db:
            file_id = image_model.file_id
            for style in image_model.styles:
                cache.sadd(style, file_id)

    @classmethod
    def exist_image(cls, file_id: str):
        return bool(cache.sismember(cls.file_list_key, file_id))

    @classmethod
    def exist_output_image(cls, file_id: str, style: str):
        return bool(cache.sismember(style, file_id))
