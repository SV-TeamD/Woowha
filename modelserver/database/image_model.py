from sqlalchemy import Column, String, ARRAY
from sqlalchemy.ext.mutable import Mutable
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class MutableList(Mutable, list):
    def append(self, value):
        list.append(self, value)
        self.changed()

    def pop(self, index=0):
        value = list.pop(self, index)
        self.changed()
        return value

    @classmethod
    def coerce(cls, key, value):
        if isinstance(value, MutableList):
            return value
        if isinstance(value, list):
            return MutableList(value)
        return Mutable.coerce(key, value)


class ImageModel(Base):
    __tablename__ = "images"

    filename = Column(String(100), primary_key=True)
    styles = Column(MutableList.as_mutable(ARRAY(String, dimensions=1)), nullable=False)

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
