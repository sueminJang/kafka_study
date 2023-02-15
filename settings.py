from pydantic import BaseSettings


class Settings(BaseSettings):
    topic: str = "test1"
    topic_2: str = "test2"
    topic_3: str = "test3"
    topic_4: str = "test4"
    host: str = "localhost"
    port: int = 9092

    class Config:
        env_file = '.env'


settings = Settings()
