"""
Lesson 7: High-Level Asynchrony via 'asyncio' and native 'async/await' Syntax.

This program demonstrates the peak of Python's cooperative multitasking evolution.
It wraps low-level selector-driven architecture into clean, human-readable keywords,
enabling non-blocking concurrent I/O operations without manual frame manipulation.

Key Features:
- Native Coroutine Definitions: Uses 'async def' to declare non-blocking execution blocks
  that yield control implicitly when encountering an expression managed by 'await'.
- Cooperative Execution Interruption: Implements 'asyncio.sleep()' to release the thread
  voluntarily, allowing the event loop dispatcher to process other ready tasks.
- Concurrent Task Aggregation: Utilizes 'asyncio.gather()' to bundle multiple coroutines
  into single-execution tasks, driving the total execution time down to the slowest job.
- Zero-Setup Lifecycle Management: Uses 'asyncio.run()' as the unified entry point,
  automatically creating, running, managing, and closing the under-the-hood Event Loop.
"""

import random
import asyncio

async def climate_sensor(room: str):
    await asyncio.sleep(1)
    temp = random.randint(0, 50)
    return f"In {room} room is {temp} ℃"
    
async def security_sensor(is_on: bool):
    await asyncio.sleep(2)
    if is_on:
        return "[INFO]: There's nothing wrong with your security system"
    return "[WARNING]: As soon as possible turn the security system!"

async def weather_sensor(city: str):
    await asyncio.sleep(3)
    temp = random.randint(-50, 50)
    return f"In {city} today is {temp} ℃. Be careful!"
    
async def launch():
    climate_result = await asyncio.gather(
        climate_sensor("Kitchen"),
        climate_sensor("Launch zone"),
        climate_sensor("Bedroom"),
        security_sensor(True),
        security_sensor(False),
        weather_sensor("Astana"),
        weather_sensor("Los-Angeles"),
    )

    return climate_result

if __name__ == "__main__":
    print(asyncio.run(launch()))
    