import os
from dataclasses import dataclass
from typing import Final

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "dev"


@dataclass
class Config:
    sqlalchemy_database_uri: Final[str] = os.getenv("DATABASE_URL")
    sqlalchemy_track_modifications: Final[bool] = False
