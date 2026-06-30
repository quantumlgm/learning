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
import random

app = FastAPI()


@app.get("/empolyees")
def get_employees(departament: str | None = None, limit: int = 3):
    return [
        {
            "employee_id": random.randint(0, 9999),
            "role": random.choice(["Backend", "DevOps", "Frontend"]),
            "departament": departament
            if departament
            else random.choice(["IT", "HR", "Finance", "Marketing"]),
        }
        for _ in range(limit)
    ]


if __name__ == "__main__":
    uvicorn.run("03_query_params:app", reload=True)
