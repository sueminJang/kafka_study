from confluent_kafka import Consumer

from basic.consumer import get_message
from config import ConsumerConfig
from settings import settings

c = Consumer(**ConsumerConfig().dict(by_alias=True))

c.subscribe([settings.topic])

get_message()
