from fastapi import FastAPI
from pydantic import BaseModel

from fake_db import employees_db

app = FastAPI()

class EmployeeSchema(BaseModel):
    salary: float
    internal_token: str
    first_name: str
    last_name: str
    departament: str
    skills: list[str] = []

@app.post("/employees", status_code=201)
def create_employe(data: EmployeeSchema):
    new_data = data.model_dump()
    new_data["id"] = len(employees_db) + 1
    employees_db.append(data)


if __name__ == "__main__":
    uvicorn.run("06_status_codes_exceptions:app", reload=True)
