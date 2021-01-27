from flask import request
from . import metrics


class MetricsRegister:
    common_counter = metrics.counter(
        "flask_by_endpoint_counter",
        "Request count by endpoints",
        labels={"endpoint": lambda: request.endpoint},
    )

    @classmethod
    def register_defaults(cls):
        # register additional default metrics
        metrics.register_default(
            metrics.counter(
                "flask_by_path_counter",
                "Request count by request paths",
                labels={"path": lambda: request.path},
            )
        )
