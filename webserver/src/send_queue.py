import time
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)


class sendQueue:
    def send_url(self, message):
        while True:
            channel.basic_publish(
                exchange="",
                routing_key="task_queue",
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                ),
            )
        print(" [x] Sent %r" % message)
        time.sleep(0.8)


connection.close()