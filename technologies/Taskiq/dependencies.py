from typing import AsyncGenerator

from taskiq import Context, TaskiqDepends

from service import FakeDatabaseConnection


async def get_db_session() -> AsyncGenerator:
    conn = FakeDatabaseConnection()
    try:
        yield conn
        await conn.commit()
    except Exception as e:
        await conn.rollback()
        raise e
    finally:
        await conn.close()
