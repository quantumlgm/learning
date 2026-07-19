"""
Lesson 10: Seamless Integration of FastAPI, SQLAlchemy 2.0, and Pydantic v2.

This code demonstrates how to securely expose database records via an API layer
using Data Transfer Objects (DTOs) to manage validation and prevent recursion.

Key Concepts Implemented:
1. Pydantic DTO Configuration: Utilizes ConfigDict(from_attributes=True) to allow
   Pydantic models to automatically extract and validate fields directly from SQLAlchemy ORM objects.
2. Flat API Response: Defines WorkerDTO to output simple, secure worker records 
   without exposing deeper relational data or sensitive database columns.
3. Nested Relational Response: Implements WorkerRelDTO which nests ResumeDTO to properly 
   serialize complex one-to-many relationship structures into clean hierarchical JSON.
4. Eager Loading in Endpoints: Couples FastAPI routes with explicit selectinload options
   to guarantee all related collections are pre-fetched within the session transaction.
"""

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    selectinload,
    sessionmaker,
)
from config import settings


app = FastAPI()

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

    resumes: Mapped[list["ResumesOrm"]] = relationship(back_populates="worker")


class ResumesOrm(Base):
    __tablename__ = "resumes_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers_orm.id"))

    worker: Mapped["WorkersOrm"] = relationship(back_populates="resumes")


def create_tables():
    Base.metadata.create_all(engine)


class ResumeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    worker_id: int


class WorkerDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    age: int


class WorkerRelDTO(WorkerDTO):
    resumes: list[ResumeDTO]


@app.get("/workers", response_model=list[WorkerDTO])
def get_workers():
    with sessionf() as session:
        stmt = select(WorkersOrm)
        res = session.execute(stmt).scalars().all()
        return res


@app.get("/workers/{worker_id}", response_model=WorkerRelDTO)
def get_worker_with_resumes(worker_id: int):
    with sessionf() as session:
        stmt = (
            select(WorkersOrm)
            .options(selectinload(WorkersOrm.resumes))
            .where(WorkersOrm.id == worker_id)
        )
        res = session.execute(stmt).scalar_one_or_none()
        return res