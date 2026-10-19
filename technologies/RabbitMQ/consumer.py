import asyncio
import json
import aio_pika
from loguru import logger

RMQ_URL = "amqp://guest:guest@127.0.0.1:5672/"
EXCHANGE_NAME = "my_exchange"
QUEUE_NAME = "tasks_queue"


async def main():
    connection = await aio_pika.connect_robust(RMQ_URL)
    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        exchange = await channel.declare_exchange(
            name=EXCHANGE_NAME,
            type=aio_pika.ExchangeType.DIRECT,
            durable=True
        )

        queue = await channel.declare_queue(
            name=QUEUE_NAME,
            durable=True
        )
        await queue.bind(exchange, routing_key="tasks")

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    payload = json.loads(message.body.decode("utf-8"))
                    logger.info(f"Received task: {payload['task_id']}, Connection: {payload['connection']}")
                    await asyncio.sleep(2)  

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Consumer stopped.")                    