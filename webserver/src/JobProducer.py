import pika


parameters = pika.ConnectionParameters("rabbitmq")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


class JobProducer:
    def __init__(self):
        channel.queue_declare(queue="job_queue", durable=True)

    def add_job(self, message):
        print("add job in queue {}".format(message))
        channel.basic_publish(
            exchange="",
            routing_key="job_queue",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print("Sent {}".format(message))

    def close_connection(self):
        connection.close()
