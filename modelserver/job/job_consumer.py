import json
import os

import pika

from network.Runner import Runner

INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()
runner = Runner(input_dir=INPUT_FOLDER, output_dir=OUTPUT_FOLDER)


class JobConsumer:
    @classmethod
    def __init__(cls):
        channel.queue_declare(queue="job_queue", durable=True)
        channel.basic_qos(prefetch_count=1)
        print("hi Job Consumer")

    @classmethod
    def generate_image(cls, _channel, method, _, body):
        try:
            message = json.loads(body)
            print(" [x] Received {}".format(body.decode()))
            runner.run(
                imagefile_name=message["filename"], style=message["author"]
            )  # GAN run (generate image)
            print(" [x] Done")
            _channel.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(e)
            _channel.basic_reject(delivery_tag=method.delivery_tag, requeue=False)

    @classmethod
    def start(cls):
        channel.basic_consume(
            queue="job_queue", auto_ack=False, on_message_callback=cls.generate_image
        )
        channel.start_consuming()

    @classmethod
    def close_connection(cls):
        connection.close()


if __name__ == "__main__":
    jc = JobConsumer()
    jc.start()
