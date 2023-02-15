from confluent_kafka import Consumer

from config import ConsumerConfig
from settings import settings

c = Consumer(**ConsumerConfig().dict(by_alias=True))
c.subscribe([settings.topic])


def get_message():
    while True:
        msg = c.poll(1)
        if msg is None:
            continue
        print(msg.value().decode())


get_message()
