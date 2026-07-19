from fastapi import FastAPI
from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,    
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