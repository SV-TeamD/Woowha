from . import db


class ImageModel(db.Model):
    __tablename__ = "images"

    filename = db.Column(db.String(20), primary_key=True)
    styles = db.Column(db.ARRAY(db.String, dimensions=1), nullable=False)

    def __init__(self, filename: str, styles: str):
        self.filename = filename
        self.styles = styles

    def __repr__(self):
        return "<ImageModel %r>" % self.styles

    @classmethod
    def serialize(cls):
        return {
            "filename": cls.filename,
            "styles": cls.styles,
        }
