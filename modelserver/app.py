from job.JobConsumer import JobConsumer

jobConsumer = JobConsumer()


class App:
    def __init__(self):
        pass

    def run(self):
        jobConsumer.start()


if __name__ == "__main__":
    app = App()
    app.run()
