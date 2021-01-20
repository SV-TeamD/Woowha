import json
import os

import pika

from network.Runner import Runner

INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")

parameters = pika.ConnectionParameters("rabbitmq")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
runner = Runner(input_dir=INPUT_FOLDER, output_dir=OUTPUT_FOLDER)


# TODO: MessageQueue abstract 만들고 상속하자
class JobConsumer:
    @classmethod
    def __init__(cls):
        channel.queue_declare(queue="job_queue", durable=True)
        channel.basic_qos(prefetch_count=1)
        print("hi Job Consumer")

    @classmethod
    def generate_image(cls, _channel, method, _, body):
        message = json.loads(body)
        print(" [x] Received {}".format(body.decode()))
        # TODO: generate image
        runner.run(imagefile_name=message["filename"], style=message["author"])
        print(" [x] Done")
        _channel.basic_ack(delivery_tag=method.delivery_tag)

    @classmethod
    def start(cls):
        channel.basic_consume(queue="job_queue", on_message_callback=cls.generate_image)
        channel.start_consuming()

    @classmethod
    def close_connection(cls):
        connection.close()


if __name__ == "__main__":
    jc = JobConsumer()
    jc.start()
