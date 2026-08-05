import json
import asyncio
from fastapi import FastAPI, HTTPException
from redis.asyncio import Redis
import uvicorn

app = FastAPI()

redis = Redis.from_url("redis://localhost:6379", decode_responses=True)

fake_database = {
    "categories": [
        {"id": 1, "name": "Electronics"},
        {"id": 2, "name": "Clothing"},
        {"id": 3, "name": "Books"},
    ]
}

CACHE_KEY = "categories_list"
TTL_SECONDS = 60


@app.get("/categories", tags=["categories"])
async def get_categories():
    cached_data = await redis.get(CACHE_KEY)

    if cached_data:
        print("⚡ [REDIS] Данные взяты из КЭША!")
        return json.loads(cached_data)

    print("🐢 [DATABASE] Кэша нет! Идем в БД...")
    await asyncio.sleep(2)
    categories = fake_database["categories"]

    await redis.set(CACHE_KEY, json.dumps(categories), ex=TTL_SECONDS)

    return categories


@app.post("/categories", tags=["categories"])
async def create_category(name: str):
    new_id = len(fake_database["categories"]) + 1
    new_category = {"id": new_id, "name": name}
    fake_database["categories"].append(new_category)

    await redis.delete(CACHE_KEY)
    print("🗑️ [REDIS] Кэш инвалидирован!")

    return new_category


@app.delete("/categories/{category_id}", tags=["categories"])
async def delete_category(category_id: int):
    fake_database["categories"] = [
        c for c in fake_database["categories"] if c["id"] != category_id
    ]

    await redis.delete(CACHE_KEY)
    print("🗑️ [REDIS] Кэш инвалидирован!")

    return {"status": "deleted", "id": category_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
