import redis.asyncio as aioredis
import asyncio

async def main():
    redis = aioredis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

    try:
        pipe = redis.pipeline(transaction=True)

        pipe.set("user:200:name", "Bob")
        pipe.set("user:200:age", 30)
        pipe.incr("user:200:visits")
        pipe.get("user:200:name")

        res = await pipe.execute()

        print(f"Result: {res}")

    finally:
        await redis.aclose()

if __name__ == "__main__":
    asyncio.run(main())