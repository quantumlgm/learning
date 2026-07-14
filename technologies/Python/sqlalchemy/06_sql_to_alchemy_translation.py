"""
Lesson 6: Translating Complex SQL Queries to SQLAlchemy ORM Expression Language.

This program demonstrates how to convert raw SQL queries into clean SQLAlchemy
constructs using advanced select features, function mappings, and debugging tools.

Key Features:
- Advanced Columns Projection: Building target SELECT queries with specific column
  attributes instead of retrieving entire ORM model instances.
- DB-Side Type Casting: Utilizing 'cast()' to explicitly convert data types (e.g.,
  Integer to String/VARCHAR) directly within the database execution scope.
- Result Aliasing: Applying '.label()' to dynamically assign custom names (AS)
  to columns and expressions in the returning payload.
- Multi-Condition Filtering: Chaining logical constraints using the 'and_' operator
  combined with column string operations like '.contains()' (LIKE pattern matching).
- SQL Debugging and Compilation: Compiling SQLAlchemy query objects into raw, dialect-specific
  SQL strings using '.compile(compile_kwargs={"literal_binds": True})' to view the
  exact parameters being sent to PostgreSQL.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import (
    String,
    and_,
    create_engine,
    select,
    cast,
)
from config import settings


engine = create_engine(settings.DB_URL_psycopg)


sessionf = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class WorkersOrm(Base):
    __tablename__ = "workers_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
    age: Mapped[int]


def advanced_select():
    with sessionf.begin() as session:
        stmt = (
            select(
                WorkersOrm.username, cast(WorkersOrm.age, String).label("age_varchar")
            )
            .select_from(WorkersOrm)
            .filter(and_(WorkersOrm.age > 18, WorkersOrm.username.contains("Linus")))
            .group_by(WorkersOrm.username, WorkersOrm.age)
        )
        print(stmt.compile(compile_kwargs={"literal_binds": True}))
        """
        SELECT workers_orm.username, CAST(workers_orm.age AS VARCHAR) AS age_varchar 
        FROM workers_orm 
        WHERE workers_orm.age > 18 AND (workers_orm.username LIKE '%' || 'Linus' || '%') GROUP BY workers_orm.username
        """

        res = session.execute(stmt)
        print(res.all())
        """
        [('Linus Torvalds', '40')]
        """


advanced_select()
