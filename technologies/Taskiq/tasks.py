from taskiq import TaskiqDepends
from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend

from dependencies import get_db_session
from service import FakeDatabaseConnection


redis = RedisAsyncResultBackend(redis_url="redis://localhost:6379", result_ex_time=300)

broker = AioPikaBroker("amqp://guest:guest@localhost:5672/").with_result_backend(redis)


@broker.task
async def save_user_order(
    order_id: int,
    shoud_fall: bool = False,
    db: FakeDatabaseConnection = TaskiqDepends(get_db_session),
): 
    if shoud_fall is True:
        print("[TASK]: Произошла ошибка")
        raise ZeroDivisionError("Simulated error")
    print(f"[TASK]: Заказ {order_id} выполнен")


