from celery import Celery


celery = Celery("demo", broker="amqp://celery:celerypass@localhost:5672//")


@celery.task
def add(x: int, y: int) -> int:
    print(f"Вычисление {x} и {y}")
    result = x + y
    print(f"{x} + {y} = {result}")
    return result