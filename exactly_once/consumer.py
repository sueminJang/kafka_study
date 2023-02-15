from confluent_kafka import Consumer

from basic.consumer import get_message
from config import ConsumerConfig
from settings import settings

c = Consumer(**ConsumerConfig(
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    isolation_level="read_committed",
).dict(by_alias=True))
c.subscribe([settings.topic])

get_message()
