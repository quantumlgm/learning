"""
Lesson 1: Database Connections and Raw SQL Execution via Engine.

This program demonstrates the establishment of both synchronous and asynchronous database connections
using SQLAlchemy engines, executing raw SQL queries directly through connection pools.

Key Features:
- Engine Configuration and Pooling: Establishes decoupled synchronous ('create_engine') and asynchronous
  ('create_async_engine') endpoints, managing connection pool behavior via 'pool_size' and 'max_overflow'.
- Connection vs. Transaction Contexts: Illustrates the 'Commit-as-you-go' strategy via '.connect()'
  requiring manual confirmation, contrasted with the automated 'Begin-Once' atomic transaction block via '.begin()'.
- Raw SQL Interpretation: Demonstrates the mandatory usage of the 'text()' construct to sanitize and
  prepare explicit SQL command strings before pushing them to the database dialect layer.
- Asynchronous Concurrency: Leverages 'async with' and the 'await' protocol to execute non-blocking DML
  statements ('INSERT') using the 'asyncpg' driver under the 'asyncio' event loop framework.
"""

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, text
from config import settings

engine = create_engine(
    url=settings.DB_URL_psycopg,
    # echo=True,
    pool_size=5,
    max_overflow=10,
)

aengine = create_async_engine(
    url=settings.DB_URL_asyncpg,
    # echo=True,
    pool_size=5,
    max_overflow=10,
)

with engine.connect() as conn:
    res = conn.execute(text("select * from ships"))
    print(res.all())
    conn.commit()

with engine.begin() as conn:
    conn.execute(
        text(
            """
        update ships
        set model = 'Aurora Extra'
        where id = 3
        """
        )
    )

"""
WARNING:
This approach has a security vulnerability. This 
query is affected by SQL injection. This example 
is only intended to demonstrate how an async INSERT 
query works. To avoid this problem, it is recommended 
to use parameterized queries.
"""


async def insert_ships(courier_id: int, model: str, speed: int):
    async with aengine.begin() as conn:
        await conn.execute(
            text(
                f"""
            insert into ships(courier_id, model, speed)
            values({courier_id}, '{model}', {speed})
            """
            )
        )


asyncio.run(insert_ships(courier_id=2, model="Exceed Sunny", speed=1200))
"""
This query works properly and successfully inserts
these data into the table
"""
