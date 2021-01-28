from werkzeug.exceptions import BadRequest
from flask import json, Request, _request_ctx_stack


class JSONBadRequest(BadRequest):
    def get_body(self, environ=None):
        """Get the JSON body."""
        return json.dumps(
            {
                "code": self.code,
                "name": self.name,
                "description": self.description,
            }
        )

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]


def on_json_loading_failed(e):
    ctx = _request_ctx_stack.top
    if ctx is not None and ctx.app.config.get("DEBUG", False):
        raise JSONBadRequest("Failed to decode JSON object: {0}".format(e))
    raise JSONBadRequest()


Request.on_json_loading_failed = on_json_loading_failed
