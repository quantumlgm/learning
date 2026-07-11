from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from config import settings

engine = create_engine(
    url=settings.DB_URL_psycopg, pool_size=5, echo=True, max_overflow=10
)

metadata_obj = MetaData()

employees_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("age", Integer),
)


def create_tables():
    metadata_obj.create_all(engine)


create_tables()
