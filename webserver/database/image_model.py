from . import db


class ImageModel(db.Model):
    __tablename__ = "images"

    file_id = db.Column(db.String(16), primary_key=True)
    styles = db.Column(db.ARRAY(db.String, dimensions=1), nullable=False)

    def __init__(self, file_id: str, styles: str):
        self.file_id = file_id
        self.styles = styles

    def __repr__(self):
        return "<ImageModel %r>" % self.styles

    @classmethod
    def serialize(cls):
        return {
            "file_id": cls.file_id,
            "styles": cls.styles,
        }
