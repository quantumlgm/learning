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
