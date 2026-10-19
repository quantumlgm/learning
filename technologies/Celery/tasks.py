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
