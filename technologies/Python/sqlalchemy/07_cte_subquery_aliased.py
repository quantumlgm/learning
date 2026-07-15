from sqlalchemy.orm import Mapped, aliased, mapped_column, DeclarativeBase, relationship, sessionmaker
from sqlalchemy import (
    ForeignKey,
    Integer,
    String,    
    create_engine,
    func,
    select,    
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

class ResumesOrm(Base):
    __tablename__ = "resumes_orm"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers_orm.id'))

    worker: Mapped["WorkersOrm"] = relationship()

def join_cte_subquery_window():
    wo = aliased(WorkersOrm)
    ro = aliased(ResumesOrm)

    subq = (
        select(
            wo.id.label("worker_id"),
            wo.username,
            wo.age,
            ro.title.label("resume_title"),
            func.avg(wo.age)
            .over(partition_by=wo.age)
            .cast(Integer)
            .label("avg_age_group")
        )        
        .join(ro, ro.worker_id == wo.id)        
        .subquery("get_age")
    )

    cte = (
        select(
            subq.c.worker_id,
            subq.c.username,
            subq.c.age,
            subq.c.resume_title,
            subq.c.avg_age_group
        )
        .where(subq.c.age > 18)
        .cte("helper_age_cte")
    )

    stmt = (
        select(
            cte.c.username,
            cte.c.resume_title,
            cte.c.age,
            cte.c.avg_age_group
        )
        .order_by(cte.c.age.desc())
    )

    print(stmt.compile(compile_kwargs={"literal_binds": True}))