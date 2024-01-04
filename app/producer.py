from kafka import KafkaProducer


class TestProducer():
    def __init__(self, topic):
        self.producer = KafkaProducer(bootstrap_servers='kafka')
        self.topic = topic

    def produce(self, message):
        self.producer.send(self.topic, message.encode('utf-8'))
