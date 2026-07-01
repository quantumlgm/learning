from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from fake_db import employees_db

app = FastAPI()


class EmployeeSchemaIn(BaseModel):
    salary: float
    internal_token: str
    first_name: str
    last_name: str
    department: str
    skills: list[str] = []


class EmployeeSchemaOut(BaseModel):
    first_name: str
    last_name: str
    department: str
    skills: list[str] = []


@app.post("/employees", status_code=201)
def create_employe(data: EmployeeSchemaIn):
    new_data = data.model_dump()
    new_data["employee_id"] = len(employees_db) + 1
    employees_db.append(data)


@app.get("/employees/{employee_id}", response_model=EmployeeSchemaOut)
def get_employee(employee_id: int):
    for employee in employees_db:
        if employee["employee_id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("06_status_codes_exceptions:app", reload=True)
