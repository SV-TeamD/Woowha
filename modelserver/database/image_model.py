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
        if not isinstance(value, MutableList):
            if isinstance(value, list):
                return MutableList(value)
            return Mutable.coerce(key, value)
        else:
            return value


class ImageModel(Base):
    __tablename__ = "images"

    file_id = Column(String(16), primary_key=True)
    styles = Column(MutableList.as_mutable(ARRAY(String, dimensions=1)), nullable=False)

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
