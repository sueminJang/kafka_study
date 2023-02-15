from confluent_kafka.admin import AdminClient, NewTopic

from config import CommonKafkaConfig

a = AdminClient(CommonKafkaConfig().dict(by_alias=True))

topic = input()
new_topic = NewTopic(topic, num_partitions=3, replication_factor=1)
fs = a.create_topics([new_topic])

for topic, f in fs.items():
    try:
        f.result()
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))