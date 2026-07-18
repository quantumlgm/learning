"""
Lesson 9: Advanced ORM Relationships, Custom Joins, and DB Constraints in SQLAlchemy 2.0.

This code explores industrial patterns for configuring bi-directional relationships,
applying granular filtering at the model level, and enforcing database integrity.

Key Concepts Implemented:
1. Bidirectional Relations ('back_populates'): Establishes explicit, type-safe
   two-way data synchronization between WorkersOrm and ResumesOrm in Python memory.
2. Custom Filtering ('primaryjoin'): Features 'resumes_adult' which filters associated
   records directly in SQL (compensation > 50000) and orders them via descending IDs.
3. Eager Join Hijacking ('contains_eager'): Optimizes performance by using a manual
   SQL JOIN combined with contains_eager() to populate relationship attributes without
   triggering extra hidden queries.
4. Database Constraints & Performance: Adds a B-Tree index ('title_idx') for rapid
   string lookups and a structural 'CheckConstraint' to prevent negative compensation values.
"""

from rich import print
from sqlalchemy import (
    CheckConstraint,
    ForeignKey,
    Index,
    String,
    create_engine,
    desc,
    select,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    contains_eager,
    mapped_column,
    relationship,
    selectinload,
    sessionmaker,
)
from config import settings


engine = create_engine(settings.DB_URL_psycopg, echo=True)


sessionf = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    def __repr__(self):
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {','.join(cols)}>"


class WorkersOrm(Base):
    __tablename__ = "workers_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
    age: Mapped[int]

    resumes: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker",
        # backref="worker"
    )
    """
    backref="..." is implicit approach for make relationships. 
    When we use a backref in one table, we don't need to use it
    in other table
    """
    resumes_adult: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker",
        primaryjoin="and_(WorkersOrm.id == ResumesOrm.worker_id, ResumesOrm.compensation > 50000)",
        order_by="ResumesOrm.id.desc()",
        # lazy="selectin"
    )
    """
    If we use selectin type of uploading,
    then we shouldn't specify this type in
    query options. And this is bad practice, 
    in that it isn't explictly
    """


class ResumesOrm(Base):
    __tablename__ = "resumes_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    compensation: Mapped[int]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers_orm.id"))

    worker: Mapped["WorkersOrm"] = relationship(back_populates="resumes")

    __table_args__ = (
        Index("title_idx", "title"),
        CheckConstraint("compensation >= 0", name="check_compensation"),
    )


def create_tables():
    Base.metadata.create_all(engine)


create_tables()


def age_select():
    with sessionf.begin() as session:
        stmt = select(WorkersOrm).options(selectinload(WorkersOrm.resumes_adult))
        res = session.execute(stmt).scalars().all()
        print(res)


age_select()


def contains_eager_select():
    with sessionf.begin() as session:
        stmt = (
            select(WorkersOrm)
            .join(WorkersOrm.resumes)
            .options(contains_eager(WorkersOrm.resumes))
            .filter(WorkersOrm.age > 18)
            .limit(3)
        )
        res = session.execute(stmt).unique().scalars().all()
        print(res)


contains_eager_select()
