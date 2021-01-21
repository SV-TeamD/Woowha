import pika


parameters = pika.ConnectionParameters("rabbitmq")
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


class JobProducer:
    """Message Queue에 Job을 넣는다."""

    @classmethod
    def __init__(cls):
        channel.queue_declare(queue="job_queue", durable=True)

    @classmethod
    def add_job(cls, message):
        print("add job in queue {}".format(message))
        channel.basic_publish(
            exchange="",
            routing_key="job_queue",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        print("Sent {}".format(message))

    @classmethod
    def close_connection(cls):
        connection.close()
