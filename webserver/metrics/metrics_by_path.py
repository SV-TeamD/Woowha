from flask import request
from prometheus_flask_exporter import PrometheusMetrics


class Metrics:
    __metrics = PrometheusMetrics.for_app_factory()
    # common_counter = None

    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app):
        self.__metrics.init_app(app)
        self.__metrics.info("webserver", "webserver for Woowha", version="1.0.0")
        self.__register_default_counter()
        self.__register_metric_types()

    def __register_default_counter(self):
        self.__metrics.register_default(
            self.__metrics.counter(
                "webserver_by_path_counter",
                "Request count by request paths",
                labels={"path": lambda: request.path},
            )
        )

    def __register_metric_types(self):
        setattr(self, "common_counter", self.__common_counter())
        # self.common_counter = self.__common_counter()

    def __common_counter(self):
        return self.__metrics.counter(
            "flask_by_endpoint_counter",
            "Request count by endpoints",
            labels={"endpoint": lambda: request.endpoint},
        )
