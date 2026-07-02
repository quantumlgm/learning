import asyncio
from rich import print
import uvicorn
from fake_db import employees_db
from fastapi import BackgroundTasks, FastAPI, HTTPException


app = FastAPI()

employees_db = employees_db.copy()


async def generate_report(id: int, employee: dict[str, str | int]):
    await asyncio.sleep(3)
    print({"id": id, "employee": employee})


@app.delete("/employees/{employee_id}")
async def del_employee(employee_id: int, bg_tasks: BackgroundTasks):
    for employee in employees_db:
        if employee["employee_id"] == employee_id:
            employees_db.remove(employee)
            bg_tasks.add_task(generate_report, employee_id, employee)
            return {
                "status": 200,
                "detail": "Your report has sent to your email. Please wait",
            }
    raise HTTPException(status_code=404, detail="User doesn't founded")


if __name__ == "__main__":
    uvicorn.run("10_background_tasks:app", reload=True)
