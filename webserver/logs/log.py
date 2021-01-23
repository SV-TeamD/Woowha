import json
from logging.config import dictConfig


class Logger:
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app):
        config = json.load(open("./logs/logger.json"))
        dictConfig(config)
