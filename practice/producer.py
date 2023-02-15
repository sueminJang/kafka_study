from confluent_kafka import Producer
from watchfiles import watch

from config import ProducerConfig
from practice.file.message import Message
from settings import settings

p = Producer(**ProducerConfig().dict(by_alias=True))
message = Message()


def produce_callback(err, msg):
    if err is not None:
        print(f"Fail: {err}")
    else:
        print(f"Success: topic={msg.topic()}, partition={msg.partition()}")


for i, _ in enumerate(watch("practice/file/message.txt"), 1):
    values = message.get()
    print(f"{i}번째 전송")
    p.poll(0)
    p.produce(settings.topic, values.encode('utf-8'), callback=produce_callback)
    message.save_past_version()
p.flush()
