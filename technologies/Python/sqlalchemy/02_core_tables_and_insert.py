"""
Lesson 2: Database Schema Definition and Data Insertion via Core.

This program demonstrates the imperative declaration of database tables using the Core layer
of SQLAlchemy, showcasing metadata orchestration and bulk data population techniques.

Key Features:
- Schema Registration via MetaData: Utilizes the 'MetaData' container as a centralized registry
  to track and manage the structural definition of the table objects before physical execution.
- Imperative Table Definition: Constructs the 'Table' instance using explicit 'Column' declarations,
  specifying structural types like 'Integer' and 'String' along with constraints ('primary_key').
- Safe Parameterized Insertion: Leverages the 'insert()' query builder to construct safe DML statements,
  mitigating SQL injection risks through automatic query parameterization under the hood.
- Bulk DML Operations: Demonstrates high-performance multi-row data population ('Bulk Insert') by passing
  a collection of data dictionaries directly into the connection execution framework.
"""

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
