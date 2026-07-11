from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    create_engine,
    text,
    insert,
)
from config import settings


engine = create_engine(
    url=settings.DB_URL_psycopg, pool_size=5, echo=True, max_overflow=10
)


metadata_obj = MetaData()


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("age", Integer),
)


def create_tables():
    # 'drop_all' delete all that we add to metadata object
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)


create_tables()


def insert_data_raw():
    with engine.begin() as conn:
        stmt = """
        insert into workers (username, age)
        values ('Ruslan Quantum', 17)
        """
        conn.execute(text(stmt))


insert_data_raw()


def insert_data_new():
    with engine.begin() as conn:
        stmt = insert(workers_table).values(
            [
                {"username": "Ruslan Future", "age": 1700},
                {"username": "Linus Torwalds", "age": 56},
            ]
        )
        conn.execute(stmt)


insert_data_new()
