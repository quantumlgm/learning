"""
Lesson 03: Data Validation using Pydantic Models and ConfigDict

This script demonstrates data schema definition and validation techniques in
FastAPI using Pydantic. It showcases class inheritance to extend data structures,
field constraint enforcement using the Field function, and explicit validation
behavior modifications by leveraging ConfigDict to strictly forbid extra fields.

Key Concepts:
- Strict Schema Enforcement: Implementing 'ConfigDict(extra="forbid")' to reject 
  any incoming payload containing undocumented parameters, preventing payload contamination.
- Object-Oriented Schema Extension: Utilizing standard Python class inheritance 
  ('UserAge(UserData)') to reuse existing fields while introducing specialized fields.
- Fine-Grained Field Constraints: Employing Pydantic's 'Field' function with 
  numeric boundary constraints ('ge' for greater or equal, 'le' for less or equal).
- Automatic Request Body Parsing: Declaring Pydantic models directly as endpoint 
  function arguments to handle validation and serialization before function execution.
"""

from pydantic import BaseModel, Field, ConfigDict
from fastapi import FastAPI
import uvicorn

app = FastAPI()

data = {"email": "quantumlgm@gmail.com", "name": "Quantumlgm", "age": 16}


class UserData(BaseModel):
    email: str
    name: str
    model_config = ConfigDict(extra="forbid")


class UserAge(UserData):
    age: int = Field(ge=0, le=130)


users = []


@app.post("/users")
def add_users(user: UserData):
    users.append(user)
    return {"status": "ok"}


@app.get("/users")
def get_users():
    return users


if __name__ == "__main__":
    uvicorn.run("03_fastapi_pydentic:app", reload=True)
