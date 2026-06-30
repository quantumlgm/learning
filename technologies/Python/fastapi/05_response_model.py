"""
Lesson 05: Outbound Serialization and Sensitive Data Masking via Response Models

This script demonstrates secure API data output management. It focuses on
separating write-only input payloads from public read-only output responses using
distinct Pydantic schemas enforced via FastAPI's 'response_model' configuration.

Key Concepts:
- Symmetric Schema Separation: Implementing specialized 'In' and 'Out' structures
  to prevent structural leaks of cryptographic tokens or financial attributes.
- List Schema Aggregation: Utilizing standard Python 'list[Schema]' wrappers inside
  endpoint route decorators to serialize composite collections of objects.
- Transparent Field Filtering: Leveraging FastAPI's internal output interceptor pipeline
  to automatically prune unmapped storage dictionary keys before wire transmission.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class EmployeeSchemaIn(BaseModel):
    salary: float
    internal_token: str
    first_name: str
    last_name: str
    departament: str
    skills: list[str] = []


class EmployeeSchemaOut(BaseModel):
    first_name: str
    last_name: str
    departament: str
    skills: list[str] = []


employees = []


@app.post("/create/employee")
def create_employe(data: EmployeeSchemaIn):
    new_data = data.model_dump()
    new_data["id"] = len(employees) + 1
    employees.append(new_data)
    return new_data


@app.get("/empolyees", response_model=list[EmployeeSchemaOut])
def get_employees():
    return employees


if __name__ == "__main__":
    uvicorn.run("05_response_model:app", reload=True)
