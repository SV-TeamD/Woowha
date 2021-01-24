import os
import logging

import pika

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
IMAGE_QUEUE = os.getenv("IMAGE_QUEUE")
ROUTING_KEY = os.getenv("ROUTING_KEY")


class JobProducer:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, amqp_url: str = RABBITMQ_HOST):
        self._params = pika.ConnectionParameters(
            amqp_url, heartbeat=600, blocked_connection_timeout=300
        )
        self._conn = None
        self._channel = None
        self._url = amqp_url
        self.connect()

    def connect(self):
        if self._conn and not self._conn.is_closed:
            return
        self._conn = pika.BlockingConnection(self._params)
        self._channel = self._conn.channel()
        self._channel.queue_declare(queue=IMAGE_QUEUE, durable=True)

    def _publish(self, msg):
        self._channel.basic_publish(exchange="", routing_key=ROUTING_KEY, body=msg)
        self.LOGGER.info("Published message : %s", msg)

    def publish(self, msg):
        """Publish msg, reconnecting if necessary."""
        try:
            self._publish(msg)
        except Exception as e:
            self.LOGGER.warning("%s", e)
            self.LOGGER.info("Reconnecting to queue")
            self.connect()
            self._publish(msg)

    def close(self):
        if self._conn and self._conn.is_open:
            self.LOGGER.info("Closing connection")
            self._conn.close()
