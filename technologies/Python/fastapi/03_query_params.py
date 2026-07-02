"""
Lesson 03: URL Query Parameters and Dynamic Filtering

This script demonstrates how to handle optional and default string/integer
filtering parameters using HTTP Query strings (?key=value). It highlights
the structural difference between Path and Query variable parsing inside FastAPI.

Key Concepts:
- Implicit Query Detection: Function arguments missing from the decorator's
  URL path layout are automatically treated as URI query parameters.
- Default & Optional Type-Hints: Leveraging fallback assignments (e.g., limit: int = 3)
  and union types (str | None) to allow flexible client request structures.
- Structural List Comprehensions: Programmatically building realistic mock
  dataset arrays shaped natively by user-defined payload scale bounds.
"""

from fastapi import FastAPI
import uvicorn

from fake_db import employees_db

app = FastAPI()


@app.get("/empolyees", description="Departments: IT, HR, Finance, Marketing")
def get_employees(department: str | None = None, limit: int = 3):
    result = []
    for employee in employees_db:
        if employee["department"] == department:
            result.append(employee)
    return result[:limit]


if __name__ == "__main__":
    uvicorn.run("03_query_params:app", reload=True)
