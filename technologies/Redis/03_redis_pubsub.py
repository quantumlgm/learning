import redis.asyncio as aioredis
import asyncio

async def subscriber():
    redis = aioredis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    pubsub = redis.pubsub()

    await pubsub.subscribe("notifications")
    print("[Subscriber] Подписался на канал 'notifications'")
    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                channel = message["channel"]
                data = message["data"]
                print(f" [Subscriber] Получено из '{channel}': {data}")
                if data == "STOP":
                    print(" [Subscriber] Получена команда остановки.")
                    break
    finally:
        await pubsub.unsubscribe("notifications")
        await redis.aclose()


async def publisher():
    await asyncio.sleep(1)

    redis = aioredis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

    try:
        messages = ["Привет!", "Заказ №1042 оформлен", "Алиса вошла в сеть", "STOP"]

        for msg in messages:
            print(f"📤 [Publisher] Отправляю: '{msg}'")
            receivers = await redis.publish("notifications", msg)
            print(f"   └─ Доставлено подписчикам: {receivers}")

            await asyncio.sleep(1)
    finally:
        await redis.aclose()


async def main():
    await asyncio.gather(
        subscriber(),
        publisher(),
    )


if __name__ == "__main__":
    asyncio.run(main())
