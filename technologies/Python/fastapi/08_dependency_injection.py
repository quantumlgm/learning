from fastapi import Depends, FastAPI
import uvicorn
from fake_db import employees_db


app = FastAPI()

def pagination(limit: int = 10, skip: int = 0):
    return {"limit": limit, "skip": skip}

async def security_session():
    print("Security check start")
    yield
    print("Security check end")

@app.get("/employees")
async def get_employees(pagination: dict[str, int] = Depends(pagination), session: None = Depends(security_session)):
    return employees_db[pagination["skip"] : pagination["limit"] + pagination["skip"]]

if __name__ == "__main__":
    uvicorn.run("08_dependency_injection:app", reload=True)