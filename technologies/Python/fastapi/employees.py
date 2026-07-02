from fastapi import APIRouter
from pydantic import BaseModel
from fake_db import employees_db


employee_router = APIRouter(prefix="/employee", tags=["Employee"])


@employee_router.get("/")
def get_employees():
    return employees_db


class EmployeeSchema(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    department: str
    role: str
    salary: int | float
    internal_token: str
    skills: list[str]


@employee_router.post("/create")
def create_employe(data: EmployeeSchema):
    new_data = data.model_dump()
    new_data["id"] = len(employees_db) + 1
    employees_db.append(new_data)
    return new_data
