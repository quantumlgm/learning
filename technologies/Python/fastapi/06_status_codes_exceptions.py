"""
Lesson 06: Custom Status Codes and Conditional Exception Handling

This script demonstrates explicit control over HTTP response statuses and
error propagation pipelines. It implements structured validation using specialized
In/Out schemas while sourcing data from an isolated external mock dataset module.

Key Concepts:
- HTTP Status Constraints: Customizing default route signaling by forcing standard
  semantic responses (e.g., 201 Created) inside the route path operational mapping.
- Procedural Exception Interrupts: Short-circuiting the request execution tree using
  'HTTPException' constructs to safely emit semantic status failures (404 Not Found).
- External Module Data Sourcing: Abstracting mock repository dependencies out of the
  primary application context while managing clean serialization over internal array dicts.
"""

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
    employees_db.append(new_data)
    return new_data


@app.get("/employees/{employee_id}", response_model=EmployeeSchemaOut)
def get_employee(employee_id: int):
    for employee in employees_db:
        if employee["employee_id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("06_status_codes_exceptions:app", reload=True)
