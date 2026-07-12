from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import Mapped, Session, mapped_column, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from config import settings


# Create sync engine
engine = create_engine(
    url=settings.DB_URL_psycopg, pool_size=5, echo=True, max_overflow=10
)


# Create asynchronous engine
aengine = create_async_engine(
    url=settings.DB_URL_asyncpg,
    pool_size=5,
    max_overflow=10,
)


# Bad practice for open session
with Session(engine) as session:
    pass


"""
Good practice for open session, here is created factory 
of sessions, and we can open it when we need to do something
within database
"""
sessionf = sessionmaker(engine, expire_on_commit=False)
with sessionf() as session:
    pass

"""
OR we can use asynchronous approach
"""
asessionf = async_sessionmaker(aengine, expire_on_commit=False)
async def async_session():
    async with asessionf() as asession:
        pass


# Create orm database
class Base(DeclarativeBase):
    pass


class WorkersOrm(Base):
    __tablename__ = "workers_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    age: Mapped[int]


# Attempt to insert data into our ORM table 
def insert_data():
    worker = WorkersOrm(username="Ruslan Orm", age=17)
    with sessionf() as session:
        session.add(worker)
        session.commit()
