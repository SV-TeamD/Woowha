from utils import _Utils, OUTPUT_FOLDER
from . import db
from .image_model import ImageModel
from .utils import SQLAlchemyDBConnection

"""Table "public.images"

  Column  |          Type          | Collation | Nullable | Default
----------+------------------------+-----------+----------+---------
 filename | character varying(100) |           | not null |
 styles   | character varying[]    |           | not null |
Indexes:
    "images_pkey" PRIMARY KEY, btree (filename)

filename:  daa24daad3393865.jpg
styles:  {cartoongan_hayao, cartoongan_hosoda}
"""

class Database:
    @classmethod
    def sync_image_models(cls):
        with SQLAlchemyDBConnection(db) as session:
            files = []
            print(_Utils.file_from_storage(OUTPUT_FOLDER))
            for file in _Utils.file_from_storage(OUTPUT_FOLDER):
                [filename, style] = _Utils.filename_and_style(file)
                files.append([filename, style])
                exist_model = ImageModel.query.filter_by(filename=filename).first()
                if exist_model is None: # db에 없으면
                    session.add(ImageModel(filename, style)) # add
                else:
                    exist_model.styles.append(style) # db에 이미 있으면 update (style 추가)

            return files # [[filename, style]]
