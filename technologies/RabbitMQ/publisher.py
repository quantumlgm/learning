

import asyncio
import json

import aio_pika


RMQ_URL = "amqp://guest:guest@localhost:5672/"
EXCHANGE_NAME = "my_exchange"


async def main():
    connection = await aio_pika.connect_robust(RMQ_URL)
    async with connection:
        channel = await connection.channel()

        exchange = await channel.declare_exchange(
            name=EXCHANGE_NAME,
            type=aio_pika.ExchangeType.DIRECT, 
            durable=True
        )

        for i in range(1, 4):
            payload = {
                "task_id": i, 
                "connection": f"Async data {i}"
            }
            message = aio_pika.Message(
                body=json.dumps(payload).encode("utf-8"),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT
            )
            await exchange.publish(message, routing_key="tasks")

if __name__ == "__main__":    
    asyncio.run(main())