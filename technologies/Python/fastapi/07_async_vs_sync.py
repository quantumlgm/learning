"""
Lesson 07: Concurrency Architecture - Asynchronous vs Synchronous Execution

This script illustrates the internal mechanics of FastAPI's request dispatching
system. It contrasts cooperative multitasking via the Event Loop ('async def')
against blocking operation offloading via the External Thread Pool ('def').

Key Concepts:
- Event Loop Non-Blocking I/O: Utilizing 'asyncio.sleep' within 'async def' to yield
  execution control back to the loop, enabling high concurrent request scaling.
- Thread Pool Offloading: Deploying standard 'def' alongside 'time.sleep' to prove how
  FastAPI insulates the main loop from blocking routines by utilizing worker threads.
- Shared Resource Starvation: Demonstrating why mixing CPU-bound or synchronous blocking
  utilities directly inside async contexts destroys overall throughput capacity.
"""

import asyncio
import time
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/sync")
def sync_run():
    time.sleep(5)
    return {"satus": "Sync report done"}


@app.get("/async")
async def async_run():
    await asyncio.sleep(5)
    return {"status": "Async report is done"}


if __name__ == "__main__":
    uvicorn.run("07_async_vs_sync:app", reload=True)
