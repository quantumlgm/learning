from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    broker_url: str = "amqp://celery:celerypass@localhost:5672//"
    result_backend: str = "redis://localhost:6379/0"
    include: list[str] = ["tasks"]
    task_serializer: str = "json"
    task_ignore_result: bool = True
    task_track_started: bool = True


settings = Settings()
