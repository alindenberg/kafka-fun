from kafka import KafkaConsumer


class TestConsumer():
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic, bootstrap_servers='kafka', auto_offset_reset='earliest')

    def consume(self):
        for msg in self.consumer:
            print(msg)
