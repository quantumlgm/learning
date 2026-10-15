import asyncio

import httpx
from taskiq import TaskiqEvents, TaskiqState

from tasks import broker, save_user_order


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def startup_event(state: TaskiqState):
    client = httpx.AsyncClient() 
    state.http_client = client
    print("[WORKER]: Воркер начал работу")


@broker.on_event(TaskiqEvents.WORKER_SHUTDOWN)
async def shutdown_event(state: TaskiqState):
    await state.http_client.aclose()
    print("[WORKER]: Воркер заврешает работу")


async def main():
    await broker.startup()
    await save_user_order.kiq(order_id=1, shoud_fall=False)


if __name__ == "__main__":
    asyncio.run(main())
