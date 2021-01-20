from typing import List

import redis

from .image_model import ImageModel

cache = redis.Redis(host="redis", port=6379)


class Cache:
    file_list_key = "images:file_list"

    def __init__(self):
        self.load_db()

    @classmethod
    def load_db(cls):
        all_data_in_db = ImageModel.query.all()
        if not all_data_in_db:
            return
        cls.add_all_db_data(all_data_in_db)

        print("cacheing Done!!")
        print(type(cache.smembers(cls.file_list_key)))
        print(cache.smembers(cls.file_list_key))

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
    def exist_output_image(cls, file_id: str, author: str):
        return bool(cache.sismember(author, file_id))
