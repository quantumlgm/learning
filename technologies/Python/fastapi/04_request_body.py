"""
Lesson 04: HTTP POST Requests and JSON Schema Validation with Pydantic

This script demonstrates handling input data payloads enclosed in the HTTP Request Body.
It introduces defining strict validation schemas using Pydantic's 'BaseModel' and
simulates state preservation using a volatile global in-memory registry data store.

Key Concepts:
- Pydantic BaseModel Parsing: Enforcing structured JSON type-safety matching defined 
  attributes (strings and dynamic string list arrays) passed into endpoint arguments.
- Schema Attribute Access: Intercepting data fields directly from the validated schema 
  instance object using standard object-oriented dot notation.
- Mock State Tracking: Utilizing a global array list context boundary to simulate 
  incremental primary key auto-generation and row-creation mutations.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class EmployeeSchema(BaseModel):
    first_name: str
    last_name: str
    departament: str
    skills: list[str] = []

employees = []

@app.post("/create/employee")
def create_employe(data: EmployeeSchema):
    new_data = data.model_dump()
    new_data["id"] = len(employees) + 1
    employees.append(new_data)
    return new_data

@app.get("/empolyees")
def get_employees():
    return employees

if __name__ == "__main__":
    uvicorn.run("04_request_body:app", reload=True)
