from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict 
from sqlalchemy import Column, ForeignKey, MetaData, String, Table, create_engine, select
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
    skills: Mapped[list['SkillsOrm']] = relationship(
        back_populates='workers',
        secondary="worker_skills"
    )


class ResumesOrm(Base):
    __tablename__ = "resumes_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers_orm.id"))

    worker: Mapped[list["WorkersOrm"]] = relationship(back_populates="resumes")


class SkillsOrm(Base):
    __tablename__ = "skills_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    version: Mapped[str] = mapped_column(String(255))

    workers: Mapped["WorkersOrm"] = relationship(
        back_populates="skills",
        secondary="worker_skills"
    )


worker_skills = Table(
    "worker_skills",
    Base.metadata,
    Column("worker_id", ForeignKey("workers_orm.id", ondelete='cascade'), primary_key=True),
    Column("skill_id", ForeignKey("skills_orm.id", ondelete='cascade'), primary_key=True),   
)


def create_tables():
    Base.metadata.drop_all(engine)
    metadata_obj.drop_all(engine)




create_tables()
    

def add_worker_skills():
    with sessionf.begin() as session:
        skill_python = SkillsOrm(name="Python", version="Python: 3.12.10")
        skill_redis = SkillsOrm(name="Redis", version="Redis: 8")

        worker = WorkersOrm(username='Mike Dustin', age=21)

        worker.skills.append(skill_python)
        worker.skills.append(skill_redis)

        session.add(worker)        


add_worker_skills()


def get_worker():
    with sessionf.begin() as session:
        stmt = (
            select(WorkersOrm)
            .options(
                selectinload(WorkersOrm.resumes),
                selectinload(WorkersOrm.skills)
            )
            .where(WorkersOrm.id == 1)            
        )
        worker = session.execute(stmt).scalar_one_or_none()

        print(worker.resumes)
        print(worker.skills)


get_worker()