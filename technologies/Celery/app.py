from celery import Celery


celery_app = Celery(
    "demo", 
    broker="amqp://celery:celerypass@localhost:5672//",
    backend="redis://localhost:6379/0",
    include=["tasks"]
)
