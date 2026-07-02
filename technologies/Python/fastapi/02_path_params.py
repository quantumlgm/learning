"""
Lesson 02: Path Parameters and Automatic Type Validation

This script demonstrates how to capture dynamic segments from the URL path
using FastAPI. It highlights the framework's native ability to enforce
strict type constraints and handle parsing anomalies automatically.

Key Concepts:
- Path Segment Brackets: Defining dynamic route patterns via '/path/{variable_name}'.
- Data Coercion & Validation: Utilizing standard Python type hints (: int) to force
  FastAPI to convert incoming string sequences into native integers, triggering
  an automatic 422 Unprocessable Entity HTTP response upon conversion failure.
- Swagger Schema Reflection: Observing how parameter types are automatically
  mapped into the interactive OpenAPI specification documentation.
"""

from fastapi import FastAPI
import uvicorn

from fake_db import employees_db

app = FastAPI()


@app.get("/employees/{employee_id}")
def get_employees(employee_id: int):
    for employee in employees_db:
        if employee["employee_id"] == employee_id:
            return employee
        return {"status": 404, "detail": "User not found"}


if __name__ == "__main__":
    uvicorn.run("02_path_params:app", reload=True)
