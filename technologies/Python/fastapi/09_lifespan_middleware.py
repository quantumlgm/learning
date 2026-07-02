"""
Lesson 09: Global Application Lifespan and Request-Response Interception Middleware

This script sets up application-wide lifecycle hooks alongside global HTTP request
interceptors. It uses structured asynchronous context pooling to manage startup and
shutdown sequences while tracking runtime transaction velocities using middleware layers.

Key Concepts:
- Modern Application Lifespan: Employing 'asynccontextmanager' with 'yield' semantics
  to establish centralized execution boundaries before the server begins accepting traffic.
- Global Request Interception: Implementing 'http' middleware pipes using 'call_next'
  proxies to seamlessly wrap route handlers with transactional benchmarking tools.
- Response Pipeline Traversal: Guaranteeing strict downstream frame continuity by explicitly
  capturing, processing, and returning the initialized 'Response' payload instance.
"""

import asyncio
import time
from rich import print
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is open! Start your work.")
    yield
    print("Server is closed! You should have a rest.")


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def time_count(request: Request, call_next):
    start_count = time.time()
    response = await call_next(request)
    current_count = time.time() - start_count
    print(f"The request has worked for {current_count}")
    return response


@app.post("/wait")
async def wait(t: int | float):
    await asyncio.sleep(t)
    return {
        "status": 200,
        "desicion": "You can see the results of request in your server console",
    }


if __name__ == "__main__":
    uvicorn.run("09_lifespan_middleware:app", reload=True)
