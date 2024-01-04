from app.consumer import TestConsumer
from app.producer import TestProducer

if __name__ == "__main__":

    topic = "my-topic"
    consumer = TestConsumer(topic)
    producer = TestProducer(topic)

    while True:
        user_input = input("Please enter some text that we'll pass to Kafka: ")
        print(f"You entered: {user_input}, sending it to Kafka...")
        print("Sent!")
        producer.produce(user_input)
        print("Consuming...")
        consumer.consume()
