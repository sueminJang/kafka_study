from confluent_kafka import Producer

from config import ProducerConfig
from settings import settings

p = Producer(**ProducerConfig().dict(by_alias=True))


def produce_callback(err, msg):
    if err is not None:
        print(f"Fail: {err}")
    else:
        print(f"Success: topic={msg.topic()}, partition={msg.partition()}")


def send_message():
    i = 1
    while i <= 10:
        values = f"{i}번째 전송입니다"
        p.poll(0)
        p.produce(settings.topic, values.encode('utf-8'), callback=produce_callback)
        i += 1
    p.flush()


send_message()
