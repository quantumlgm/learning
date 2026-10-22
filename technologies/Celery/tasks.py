import time

from app import celery_app


@celery_app.task
def add(x: int, y: int) -> int:
    print(f"Вычисление {x} и {y}")
    result = x + y
    print(f"{x} + {y} = {result}")
    return result


@celery_app.task(bind=True)
def show_info(self, x: int) -> dict:
    return {
        "task_id": self.request.id,
        "retries": self.request.retries,
        "value": x,
    }

@celery_app.task
def slow_task(task_id: int):
    print(f"Старт задачи номер {task_id}")
    time.sleep(3)
    print(f"Конец задачи номер {task_id}")
    return task_id
