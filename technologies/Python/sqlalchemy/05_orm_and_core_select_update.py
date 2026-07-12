
from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table, create_engine, func, text, select
from config import settings
import datetime


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

def create_tables():
    metadata_obj.create_all(workers_table)


def select_workers():
    with sessionf() as session:
        with session.begin():
            stmt_select = select()