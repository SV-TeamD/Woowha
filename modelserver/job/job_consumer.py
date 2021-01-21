import json
import os

import pika
from database.postgresql import Database

from network.runner import Runner
from database.cache import Cache

INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")

parameters = pika.ConnectionParameters("rabbitmq", heartbeat=600, blocked_connection_timeout=300)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
runner = Runner(input_dir=INPUT_FOLDER, output_dir=OUTPUT_FOLDER)


class JobConsumer:
    def __init__(self):
        channel.queue_declare(queue="job_queue", durable=True)
        channel.basic_qos(prefetch_count=1)
        print("hi Job Consumer")

    @classmethod
    def start(cls):
        channel.basic_consume(queue="job_queue", auto_ack=False, on_message_callback=cls.consume)
        channel.start_consuming()

    @classmethod
    def consume(cls, _channel, method, _, body):
        print(" [x] Received {}".format(body.decode()))
        delivery_tag = method.delivery_tag
        message = json.loads(body)
        file_id = message["file_id"]
        style = message["author"]

        cls.generate_image(_channel, delivery_tag, file_id, style)
        Cache.add(file_id=file_id, author=style)
        print("{} {} saved in cache".format(file_id, style))
        if Database.select_image(file_id):
            Database.update(file_id, style)
            print("{} {} updated in database".format(file_id, style))
        else:
            Database.insert(file_id, [style])
            print("{} {} inserted in database".format(file_id, style))
        Database.select_image(file_id)

    @classmethod
    def generate_image(cls, _channel, delivery_tag, file_id, style):
        try:
            runner.run(imagefile_name="{}.jpg".format(file_id), style=style)
            print(" [x] Done")
            _channel.basic_ack(delivery_tag)
        except Exception as e:
            print(e)
            _channel.basic_reject(delivery_tag, requeue=False)

    @classmethod
    def close_connection(cls):
        connection.close()


if __name__ == "__main__":
    jc = JobConsumer()
    jc.start()
