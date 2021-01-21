from typing import List

from .image_model import ImageModel
from .utils import SQLAlchemyDBConnection


class Database:
    @classmethod
    def select_all_image(self):
        with SQLAlchemyDBConnection() as session:
            imagemodel = session.query(ImageModel)
            return imagemodel

    @classmethod
    def select_image(self, file_id: str):
        with SQLAlchemyDBConnection() as session:
            imagemodel = session.query(ImageModel).filter(ImageModel.file_id == file_id).first()
            print("select {} result : {}".format(file_id, imagemodel))
            return imagemodel

    @classmethod
    def insert(self, file_id: str, styles: List[str]):
        with SQLAlchemyDBConnection() as session:
            session.add(ImageModel(file_id, styles))

    @classmethod
    def update(self, file_id: str, style: str):
        with SQLAlchemyDBConnection() as session:
            imagemodel = session.query(ImageModel).filter(ImageModel.file_id == file_id).first()
            imagemodel.styles.append(style)
