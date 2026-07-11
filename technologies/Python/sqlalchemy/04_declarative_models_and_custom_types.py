"""
Lesson 5: Declarative Mapping, Relationships, and Reusable Column Types via Annotated.

This program demonstrates modern SQLAlchemy 2.0 declarative configuration, showcasing explicit
data typing, table relationships via Foreign Keys, and localized type reuse constraints.

Key Features:
- Declarative Mapping Architecture: Utilizes 'DeclarativeBase' and the 'Mapped' generic wrapper
  to establish strict Python type annotations that automatically align with PostgreSQL column definitions.
- Relational Schema Synchronization: Implements a one-to-many/one-to-one constraint link using the
  'ForeignKey' descriptor, enforcing cascading deletion policies ('ondelete="cascade"') directly at the database tier.
- Metadata Annotation Integration: Leverages Python's native 'typing.Annotated' to encapsulate
  reusable column attributes (such as primary keys and server-side default timestamps) within standalone type aliases.
- Centralized Data-Type Mapping: Explores the implementation of the 'type_annotation_map' registry within custom
  base classes to enforce global, database-agnostic string length limitations across multiple schemas.
"""

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey, String, create_engine, func, text
from config import settings
import enum
import datetime


engine = create_engine(
    url=settings.DB_URL_psycopg, pool_size=5, echo=True, max_overflow=10
)


class Base(DeclarativeBase):
    pass


class WorkersOrm(Base):
    __tablename__ = "workers_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    age: Mapped[int]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"
    id: Mapped[int] = mapped_column(primary_key=True)
    worker_id: Mapped[int] = mapped_column(
        ForeignKey("workers_orm.id", ondelete="cascade")
    )
    title: Mapped[str] = mapped_column(String(255))
    salary: Mapped[int | None]
    workload: Mapped[Workload]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.now()
    )


"""
For more clear code we should use Annotated and 
create new types. Due to this we can use these types
in different tables
"""

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.now()
    ),
]

string_restriction = Annotated[str, 255]


class TypeBase(DeclarativeBase):
    type_annotation_map = {string_restriction: String(255)}


class ResumesOrmClear(TypeBase):
    __tablename__ = "resumes"
    id: Mapped[intpk]
    worker_id: Mapped[int] = mapped_column(
        ForeignKey("workers_orm.id", ondelete="cascade")
    )
    title: Mapped[string_restriction]
    salary: Mapped[int | None]
    workload: Mapped[Workload]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
