import json
import os

import pika

from database.cache import Cache
from database.postgresql import Database
from network.runner import Runner

INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")

parameters = pika.ConnectionParameters("rabbitmq", heartbeat=600, blocked_connection_timeout=300)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
runner = Runner(input_dir=INPUT_FOLDER, output_dir=OUTPUT_FOLDER)


class JobConsumer:
    @classmethod
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
        filename = message["filename"]
        style = message["style"]

        try:
            cls.generate_image(_channel, delivery_tag, filename, style)
        except Exception as e:
            print(e)
            print("{}를 생성하는데 실패하였습니다.".format(filename))
            return
        Cache.add(filename=filename, style=style)
        print("{} {} saved in cache".format(filename, style))
        if Database.select_image(filename):
            Database.update(filename, style)
            print("{} {} updated in database".format(filename, style))
        else:
            Database.insert(filename, [style])
            print("{} {} inserted in database".format(filename, style))
        Database.select_image(filename)

    @classmethod
    def generate_image(cls, _channel, delivery_tag, filename, style):
        try:
            runner.run(filename, style=style)
            print(" [x] Done")
            _channel.basic_ack(delivery_tag)
        except Exception as e:
            _channel.basic_reject(delivery_tag, requeue=False)
            raise e from e

    @classmethod
    def close_connection(cls):
        connection.close()


if __name__ == "__main__":
    jc = JobConsumer()
    jc.start()
