from . import db


class ImageModel(db.Model):
    __tablename__ = "images"

    id = db.Column(db.String(16), primary_key=True)
    url = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, image_id: str, image_url: str):
        self.id = image_id
        self.url = image_url

    def __repr__(self):
        return "<ImageModel %r>" % self.url

    @classmethod
    def serialize(cls):
        return {
            "image_id": cls.id,
            "image_url": cls.url,
        }
