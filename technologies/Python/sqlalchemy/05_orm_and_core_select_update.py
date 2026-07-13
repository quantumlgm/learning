
import random
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, text, select, update
from config import settings


engine = create_engine(
    url=settings.DB_URL_psycopg, pool_size=5, echo=True, max_overflow=10
)


sessionf = sessionmaker(engine, expire_on_commit=False)


metadata_obj = MetaData()


# Data types
str_255 = Annotated[str, String(255)]


# Tables
class Base(DeclarativeBase):
    pass


# ORM Table
class WorkersOrm(Base):
    __tablename__ = "workers_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str_255]
    age: Mapped[int]


# Core Table
workers_table = Table(
    "workers_core",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(255)),
    Column("age", Integer),
)


# Create tables with core and orm approaches
def create_tables_core():
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)


create_tables_core()


def create_tables_orm():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


create_tables_orm()


# Queries for core table
def select_workers_core():
    with engine.begin() as conn:
            query = select(workers_table)
            result = conn.execute(query)
            print(f'result={result.all()}')


def update_worker_core():
    with engine.begin() as conn:
            stmt = text("update workers_core set age=:new_age where id=:id")        
            stmt = stmt.bindparams(new_age=random.randint(0, 100), id=1)
            conn.execute(stmt)            


def update_worker_core_py_approach():
    with engine.begin() as conn:
        stmt = (
            update(WorkersOrm).values(age=random.randint(0, 100))
            .filter_by(id=1)
        )
        conn.execute(stmt)        
            

# Queries for orm table
def select_worker_orm():
    with sessionf.begin() as session:        
        query = select(WorkersOrm)
        result = session.execute(query)
        print(f'result={result.all()}')

select_worker_orm()