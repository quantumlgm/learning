import redis.asyncio as aioredis
import asyncio

async def main():
    redis = aioredis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

    try:
        # Strings
        await redis.set("visits", 10)
        await redis.incrby("visits", 1)
        await redis.expire("visits", 20)

        visits = await redis.get("visits")
        ttl = await redis.ttl("visits")
        print(f'Visits: {visits}, TTL: {ttl}')

        # Hashes
        users = {
            "name": "Alex", 
            "age": "25", 
            "role": "Admin"
        }
        await redis.hset("user:100", mapping=users)
        await redis.hincrby("users:100", "age", 1)
        user_dict = await redis.hgetall("user:100")
        print(f"User Hash: {user_dict}")

        # Lists
        await redis.rpush("py_queue", "task_1", "task_2")
        task = await redis.lpop("py_queue")
        print(f"Pop from Queue: {task}")
       
        await redis.zadd("py_leaderboard", {"player_1": 100, "player_2": 250})
        await redis.zincrby("py_leaderboard", 200, "player_1")
       
        top_players = await redis.zrevrange("py_leaderboard", 0, -1, withscores=True)
        print(f"Leaderboard: {top_players}")

    finally:
        await redis.aclose()

if __name__ == "__main__":
    asyncio.run(main())


