import random
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    text,
    select,
    update,
)
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
"""
CREATE TABLE workers_core (
        id SERIAL NOT NULL, 
        username VARCHAR(255), 
        age INTEGER, 
        PRIMARY KEY (id)
)
"""


def create_tables_orm():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


create_tables_orm()
"""
CREATE TABLE workers_orm (
    id SERIAL NOT NULL, 
    username VARCHAR NOT NULL, 
    age INTEGER NOT NULL, 
    PRIMARY KEY (id)
)
"""


# Queries for core table
def select_workers_core():
    with engine.begin() as conn:
        stmt = select(workers_table)
        result = conn.execute(stmt)
        print(f"result={result.all()}")


def insert_workers_core():
    with engine.begin() as conn:
        stmt = """
        insert into workers_core(username, age)
        values('Quantumlgm', 17), ('Linus Torvalds', 40), ('Ruslan', 16)
        """
        conn.execute(text(stmt))


def update_worker_core():
    with engine.begin() as conn:
        stmt = text("update workers_core set age=:new_age where id=:id")
        stmt = stmt.bindparams(new_age=random.randint(0, 100), id=1)
        conn.execute(stmt)


def update_worker_core_py_approach():
    with engine.begin() as conn:
        stmt = update(WorkersOrm).values(age=random.randint(0, 100)).filter_by(id=1)
        conn.execute(stmt)

insert_workers_core()
"""
insert into workers_core(username, age)
values('Quantumlgm', 17), ('Linus Torvalds', 40), ('Ruslan', 16)
"""
select_workers_core()
"""
2026-07-14 14:30:21,398 INFO sqlalchemy.engine.Engine SELECT workers_core.id, workers_core.username, workers_core.age 
FROM workers_core
2026-07-14 14:30:21,398 INFO sqlalchemy.engine.Engine [generated in 0.00012s] {}
result=[(1, 'Quantumlgm', 17), (2, 'Linus Torvalds', 40), (3, 'Ruslan', 16)]
"""
update_worker_core()
"""
2026-07-14 14:30:21,400 INFO sqlalchemy.engine.Engine update workers_core set age=%(new_age)s::INTEGER where id=%(id)s::INTEGER
2026-07-14 14:30:21,400 INFO sqlalchemy.engine.Engine [generated in 0.00016s] {'new_age': 45, 'id': 1}
"""
select_workers_core()
"""
2026-07-14 14:30:21,400 INFO sqlalchemy.engine.Engine SELECT workers_core.id, workers_core.username, workers_core.age 
FROM workers_core
2026-07-14 14:30:21,400 INFO sqlalchemy.engine.Engine [cached since 0.00273s ago] {}
result=[(2, 'Linus Torvalds', 40), (3, 'Ruslan', 16), (1, 'Quantumlgm', 45)]
"""

# Queries for orm table
def select_worker_orm():
    with sessionf.begin() as session:
        stmt = select(WorkersOrm)
        result = session.execute(stmt)
        print(f"result={result.all()}")


def insert_workers_orm():
    with sessionf.begin() as session:
        stmt = [
                WorkersOrm(username='Quantumlgm', age=17),
                WorkersOrm(username='Linus Torvalds', age=40),
                WorkersOrm(username='Ruslan', age=16),
            ]
        session.add_all(stmt)
        # Or use session.add if you insert one element
        

def update_worker_orm():
    with sessionf.begin() as session:
        stmt = session.get(WorkersOrm, 1)
        stmt.username = 'QUANTUMLGM'


insert_workers_orm()
"""
2026-07-14 14:30:21,403 INFO sqlalchemy.engine.Engine INSERT INTO workers_orm (username, age) SELECT p0::VARCHAR, p1::INTEGER FROM (VALUES (%(username__0)s::VARCHAR, %(age__0)s::INTEGER, 0), (%(username__1)s::VARCHAR, %(age__1)s::INTEGER, 1), (%(username__2)s::VARCHAR, %(age__2)s::INTEGER, 2)) AS imp_sen(p0, p1, sen_counter) ORDER BY sen_counter RETURNING workers_orm.id, workers_orm.id AS id__1
"""
select_worker_orm()
"""
2026-07-14 14:30:21,406 INFO sqlalchemy.engine.Engine SELECT workers_orm.id, workers_orm.username, workers_orm.age 
FROM workers_orm
2026-07-14 14:30:21,406 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
result=[(<__main__.WorkersOrm object at 0x0000025030D48A40>,), (<__main__.WorkersOrm object at 0x0000025030D48A10>,), (<__main__.WorkersOrm object at 0x0000025030D48260>,)]
"""
update_worker_orm()
"""
2026-07-14 14:30:21,410 INFO sqlalchemy.engine.Engine UPDATE workers_orm SET username=%(username)s::VARCHAR WHERE workers_orm.id = %(workers_orm_id)s::INTEGER
2026-07-14 14:30:21,410 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {'username': 'QUANTUMLGM', 'workers_orm_id': 1}
"""
select_worker_orm()
"""
2026-07-14 14:30:21,412 INFO sqlalchemy.engine.Engine SELECT workers_orm.id, workers_orm.username, workers_orm.age 
FROM workers_orm
2026-07-14 14:30:21,412 INFO sqlalchemy.engine.Engine [cached since 0.004841s ago] {}
result=[(<__main__.WorkersOrm object at 0x0000025030D498B0>,), (<__main__.WorkersOrm object at 0x0000025030D49880>,), (<__main__.WorkersOrm object at 0x0000025030D490D0>,)]
2026-07-14 14:30:21,412 INFO sqlalchemy.engine.Engine COMMIT
"""

# Flush, expire and, refresh
def insert_workers_orm_flush():
    with sessionf() as session:
        insert_stmt = WorkersOrm(username='Flash Flush', age=28)        
        session.add(insert_stmt)
        session.flush()
        """
        This action sends all changes to the database
        but doesn't close the transaction
        """
        print("Before session.flush()")

        select_stmt = select(WorkersOrm)
        result = session.execute(select_stmt)
        print(f"result={result.all()}")

        session.commit()
        
print('-----insert_workers_orm_flush()-----')
"""
2026-07-14 14:57:14,222 INFO sqlalchemy.engine.Engine INSERT INTO workers_orm (username, age) VALUES (%(username)s::VARCHAR, %(age)s::INTEGER) RETURNING workers_orm.id
2026-07-14 14:57:14,222 INFO sqlalchemy.engine.Engine [generated in 0.00010s] {'username': 'Flash Flush', 'age':28}
"""
insert_workers_orm_flush()        
"""
Before session.flush()
2026-07-14 15:13:11,014 INFO sqlalchemy.engine.Engine SELECT workers_orm.id, workers_orm.username, workers_orm.age 
FROM workers_orm
2026-07-14 15:13:11,014 INFO sqlalchemy.engine.Engine [cached since 0.006511s ago] {}
result=[(<__main__.WorkersOrm object at 0x000001E41A23A120>,), (<__main__.WorkersOrm object at 0x000001E41A23A0F0>,), (<__main__.WorkersOrm object at 0x000001E41A239AF0>,), (<__main__.WorkersOrm object at 0x000001E418BBC470>,)]
"""

def update_workers_orm_expire():
    with sessionf() as session:
        worker = session.get(WorkersOrm, 1)

        print(worker.age)

        worker.age = 100
        session.flush()

        session.expire(worker)
        """
        This action tells SQLAlchemy that the object's data is expired.
        When you access its attributes, SQLAlchemy will fetch fresh data
        from the database using a new SELECT query.
        """

        print(f"worker.age={worker.age}")

    

update_workers_orm_expire()
"""
2026-07-14 15:35:15,965 INFO sqlalchemy.engine.Engine SELECT workers_orm.id AS workers_orm_id, workers_orm.username AS workers_orm_username, workers_orm.age AS workers_orm_age 
FROM workers_orm 
WHERE workers_orm.id = %(pk_1)s::INTEGER
2026-07-14 15:35:15,966 INFO sqlalchemy.engine.Engine [generated in 0.00036s] {'pk_1': 1}
worker.age=100
2026-07-14 15:35:15,966 INFO sqlalchemy.engine.Engine ROLLBACK
"""