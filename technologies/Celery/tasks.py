import random
import time

from app import celery_app


@celery_app.task
def add(x: int, y: int) -> int:
    print(f"Вычисление {x} и {y}")
    result = x + y
    print(f"{x} + {y} = {result}")
    return result


@celery_app.task(
    autoretry_for=(ZeroDivisionError,), 
    retry_kwargs={"max_retries": 3}, 
    retry_jitter=True
)
def divide(x: int, y: int) -> int:
    print(f"Деление {x} и {y}")
    result = x / y
    print(f"{x} / {y} = {result}")
    return int(result)


@celery_app.task(bind=True)
def show_info(self, x: int) -> dict:
    return {
        "task_id": self.request.id,        
        "value": x,
    }


@celery_app.task
def slow_task(task_id: int):
    print(f"Старт задачи номер {task_id}")
    wasted = random.randint(0, 4)
    time.sleep(wasted)
    print(f"Конец задачи номер {task_id}")
    return {
        "completed": wasted, 
        "task_id": task_id, 
        "win": f"You didn’t waste your time! Your task is {task_id}"
    }
