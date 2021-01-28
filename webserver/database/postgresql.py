import os
from typing import List

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from utils import _Utils, INPUT_FOLDER, OUTPUT_FOLDER, ALLOWED_EXTENSIONS
from .image_model import ImageModel
from .utils import SQLAlchemyDBConnection

db = SQLAlchemy()
migrate = Migrate()


class DataBase:
    @classmethod
    def input_file_list_from_storage(cls):
        file_list = os.listdir(INPUT_FOLDER)
        return [file for file in file_list if os.path.splitext(file)[-1] in ALLOWED_EXTENSIONS]

    @classmethod
    def output_file_list_from_storage(cls):
        file_list = os.listdir(OUTPUT_FOLDER)
        return [file for file in file_list if os.path.splitext(file)[-1] in ALLOWED_EXTENSIONS]

    @classmethod
    def sync_image_models(cls, image_models: List[ImageModel]):
        exist_data_in_storage = set(filter(lambda x: _Utils.exist_file(x.filename), image_models))
        no_exist_data_in_storage = set(image_models) - exist_data_in_storage
        with SQLAlchemyDBConnection(db) as session:
            for delete_image_model in no_exist_data_in_storage:
                session.delete(delete_image_model)
        return list(exist_data_in_storage)
