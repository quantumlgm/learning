import datetime
from decimal import Decimal
import enum
from typing import Annotated
from sqlalchemy import CheckConstraint, Enum, ForeignKey, Numeric, String, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, aliased, mapped_column, relationship, sessionmaker
from config import settings


engine = create_engine(settings.DB_URL_psycopg, echo=True)


session_f = sessionmaker(engine, expire_on_commit=False)


str_255 = Annotated[str, mapped_column(String(255))]
timestamp = Annotated[datetime.datetime, mapped_column(server_default=func.now())]
intpk = Annotated[int, mapped_column(primary_key=True)]
cost = Annotated[Decimal, mapped_column(Numeric(precision=5, scale=2))]


class Base(DeclarativeBase):
    pass


class Status(enum.Enum):
    not_started = "not_started"
    in_progerss = "in_progerss"
    completed = "completed"
    failed = 'failed'


class Students(Base):
    __tablename__ = 'students'
    id: Mapped[intpk]
    name: Mapped[str_255]
    register: Mapped[timestamp]
    

class Courses(Base):
    __tablename__ = 'courses'
    id: Mapped[intpk] 
    name: Mapped[str_255]
    cost: Mapped[cost]

    
class Grades(Base):
    __tablename__ = 'grades'
    id: Mapped[intpk]
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    cours_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    status: Mapped[Status] = mapped_column(default=Status.not_started)
    assessment: Mapped[int] = mapped_column(CheckConstraint("assessment >= 0 and assessment <= 100"), nullable=True)

    student: Mapped["Students"] = relationship()
    cours: Mapped["Courses"] = relationship()


def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def populate_database():
    with session_f.begin() as session:        
        stmt = [
            Students(name='Quntum'),
            Students(name='Ruslan'),
            Students(name='Linus'),
            Students(name='Michael'),
            Students(name='Donald'),

            Courses(name='Machine Learning', cost=100),
            Courses(name='Backend Developing', cost=200.5),
            Courses(name='How to grow cucumbers', cost=50),

            Grades(student_id=1, cours_id=2, status=Status.in_progerss, assessment=None),
            Grades(student_id=2, cours_id=3, status=Status.completed, assessment=99),
            Grades(student_id=3, cours_id=1, status=Status.failed, assessment=0),
            Grades(student_id=4, cours_id=3, status=Status.completed, assessment=70),
            Grades(student_id=5, cours_id=2, status=Status.not_started, assessment=40),
        ]
        session.add_all(stmt)


create_db()
populate_database()


def select_report():
    with session_f.begin() as session:
        s = aliased(Students)
        c = aliased(Courses)
        g = aliased(Grades)
        stmt = (
            select(
                c.name,
                func.avg(g.assessment)
            )
            .select_from(c)
            .join(g, c.id == g.cours_id)
            .join(s, g)
            .group_by(c.name)
        )

        print("-" * 10)
        print(
            "RESULTAT:", session.execute(stmt).all()
        )
        print("-" * 10)


select_report()
