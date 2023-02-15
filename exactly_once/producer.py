from confluent_kafka import Producer

from config import ProducerConfig
from settings import settings

p = Producer(**ProducerConfig(
    enable_idempotence=True,
    max_in_flight_requests_per_connection=3,
    acks="all",
    retries=5,
    transactional_id="exactly_once"
).dict(by_alias=True))


def produce_callback(err, msg):
    if err is not None:
        print(f"Fail: {err}")
    else:
        print(f"Success: topic={msg.topic()}, partition={msg.partition()}")


def send_message():
    while True:
        values = input()
        p.poll(0)
        p.produce(settings.topic, values.encode('utf-8'), callback=produce_callback)
    p.flush()


send_message()
