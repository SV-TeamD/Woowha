import os
from typing import Final

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "dev"

SQLALCHEMY_DATABASE_URI: Final[str] = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS: Final[bool] = False
