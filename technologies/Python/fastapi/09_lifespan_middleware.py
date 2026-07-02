import asyncio
import time

from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from loguru import logger
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Server is open! Start your work.")
    yield 
    logger.info("Server is closed! You should have a rest.")

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def time_count(request: Request, call_next):
    start_count = time.time()
    response = await call_next(request)
    current_count = time.time() - start_count
    print(f"The request has worked for {current_count}")
    return response

@app.post('/wait')
async def wait(t: int | float):
    await asyncio.sleep(t)
    return {"status": 200, "desicion": "You can see the results of request in your server console"}
    

if __name__ == "__main__":
    uvicorn.run("09_lifespan_middleware:app", reload=True)
