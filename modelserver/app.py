from database.cache import Cache
from job.job_consumer import JobConsumer


class App:
    def __init__(self):
        # ORM
        Cache()
        JobConsumer().start()


if __name__ == "__main__":
    App()
