import os

from prometheus_flask_exporter import PrometheusMetrics


os.environ["DEBUG_METRICS"] = "1"
metrics = PrometheusMetrics(app=None)
