"""
Lesson 03: Data Validation using Pydantic Models and ConfigDict

This script demonstrates data schema definition and validation techniques in 
FastAPI using Pydantic. It showcases class inheritance to extend data structures, 
field constraint enforcement using the Field function, and explicit validation 
behavior modifications by leveraging ConfigDict to strictly forbid extra fields.
"""

from pydantic import BaseModel, Field, ConfigDict
from fastapi import FastAPI
import uvicorn

app = FastAPI()

data = {
    "email": 'quantumlgm@gmail.com',
    "name": "Quantumlgm",
    "age": 16
}

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
