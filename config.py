from typing import Optional

from pydantic import BaseModel, Field

from settings import settings


class CommonKafkaConfig(BaseModel):
    bootstrap_servers: str = Field(default=f"{settings.host}:{settings.port}", alias="bootstrap.servers", description="클라이언트가 카프카 클러스트에 처음 연결하기 위한 호스트와 포트 정보")


class ProducerConfig(CommonKafkaConfig):
    # client_dns_lookup: str = Field(default="use_all_dns_ips", alias="client.dns.lookup")
    acks: str = Field(default="1")
    # buffer_memory: int = Field(default=33554432, alias="buffer.memory")
    # compression_type: Optional[str] = Field(default=None, alias="compression.type")
    enable_idempotence: bool = Field(default=False, alias="enable.idempotence")
    max_in_flight_requests_per_connection: int = Field(default=5, alias="max.in.flight.requests.per.connection")
    retries: int = Field(default=0)
    batch_size: int = Field(default=20000, alias="batch.size")
    linger_ms: int = Field(default=0, alias="linger.ms")
    transactional_id: Optional[str] = Field(default=None, alias="transactional.id")


class ConsumerConfig(CommonKafkaConfig):
    group_id: str = Field(default="test", alias="group.id")
    group_instance_id: Optional[str] = Field(default=None, alias="group.instance.id")
    heartbeat_interval_ms: int = Field(default=300, alias="heartbeat.interval.ms")
    max_partition_fetch_bytes: int = Field(default=33554432, alias="max.partition.fetch.bytes")
    session_timeout_ms: int = Field(default=10000, alias="session.timeout.ms")
    enable_auto_commit: bool = Field(default=True, alias="enable.auto.commit")
    auto_offset_reset: str = Field(default="latest", alias="auto.offset.reset")
    fetch_min_bytes: int = Field(default=1, alias="fetch.min.bytes")
    fetch_max_bytes: int = Field(default=33554432, alias="fetch.max.bytes")
    # fetch_max_wait_ms: int = Field(default=1000, alias="fetch.max.wait.ms")
    isolation_level: str = Field(default="read_uncommitted", alias="isolation.level")
    # max_poll_records: int = Field(default=10, alias="max.poll.records")
    partition_assignment_strategy: str = Field(default="range", alias="partition.assignment.strategy")
