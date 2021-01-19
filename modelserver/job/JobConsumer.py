import json
import os

import pika

from network.Runner import Runner

INPUT_FOLDER = os.getenv("INPUT_IMAGE_PATH")
OUTPUT_FOLDER = os.getenv("OUTPUT_IMAGE_PATH")

parameters = pika.ConnectionParameters("rabbitmq", heartbeat=600, blocked_connection_timeout=300)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
runner = Runner(input_dir=INPUT_FOLDER, output_dir=OUTPUT_FOLDER)


# TODO: MessageQueue abstract 만들고 상속하자
class JobConsumer:
    def __init__(self):
        channel.queue_declare(queue="job_queue", durable=True)
        channel.basic_qos(prefetch_count=1)
        print("hi Job Consumer")

    def generate_image(self, ch, method, properties, body):
        message = json.loads(body)
        print(" [x] Received {}".format(body.decode()))
        # TODO: generate image
        runner.run(imagefile_name=message["filename"], style=message["author"])
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        channel.basic_consume(queue="job_queue", on_message_callback=self.generate_image)
        channel.start_consuming()

    def close_connection(self):
        connection.close()


if __name__ == "__main__":
    jc = JobConsumer()
    jc.start()
