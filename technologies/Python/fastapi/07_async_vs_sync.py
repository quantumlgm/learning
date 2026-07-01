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
