

import select
from rich import print
from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, joinedload, mapped_column, relationship, selectinload, sessionmaker
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
    
    resumes: Mapped[list["ResumesOrm"]] = relationship()


class ResumesOrm(Base):
    __tablename__ = "resumes_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers_orm.id'))

    worker: Mapped["WorkersOrm"] = relationship()


def create_tables():
    Base.metadata.create_all(engine)
    Base.metadata.drop_all(engine)


def lazy_relation_select():
    with sessionf.begin() as session:
        stmt = (
            select(WorkersOrm)
        )

        query = session.execute(stmt)
        res = query.scalars().all()

        print(res[0].resumes)
        
        print(res[1].resumes)

        print(res[2].resumes)

        print(res[3].resumes)

print('[red]lazy_relation_select[/red]')
lazy_relation_select()

def joinedload_relation_select():
    with sessionf.begin() as session:
        stmt = (
            select(WorkersOrm).options(joinedload(WorkersOrm.resumes))
        )

        query = session.execute(stmt)
        res = query.unique().scalars().all()

        print(res[0].resumes)
        
        print(res[1].resumes)

        print(res[2].resumes)

        print(res[3].resumes)

        
print('[yellow]joinedload_relation_select[/yellow]')
joinedload_relation_select()


def selectinload_relation_select():
    with sessionf.begin() as session:
        stmt = (
            select(WorkersOrm).options(selectinload(WorkersOrm.resumes))
        )

        query = session.execute(stmt)
        res = query.unique().scalars().all()

        print(res[0].resumes)
        
        print(res[1].resumes)

        print(res[2].resumes)

        print(res[3].resumes)

        
print('[green]joined_relation_select[/green]')
selectinload_relation_select()