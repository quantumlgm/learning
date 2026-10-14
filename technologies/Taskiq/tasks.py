import asyncio

from taskiq import Context, TaskiqDepends
from taskiq_aio_pika import AioPikaBroker
from taskiq_redis import RedisAsyncResultBackend

from dependencies import get_formatter


redis = RedisAsyncResultBackend(redis_url="redis://localhost:6379", result_ex_time=300)

broker = AioPikaBroker("amqp://guest:guest@localhost:5672/").with_result_backend(redis)


@broker.task
async def notify_user(
    user_id: int,
    message: str,
    formatter = TaskiqDepends(get_formatter),
    context: Context = TaskiqDepends(),
):
    service = context.message.labels.get("source")
    formatted_text = formatter(message)
    print(f"{service} | (ID: {context.message.task_id}): {formatted_text}")
