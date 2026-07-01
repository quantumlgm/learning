"""
Lesson 08: Hierarchical Dependency Injection and Contextual Yield Lifecycles

This script introduces FastAPI's native Dependency Injection ('Depends') framework.
It showcases modularized extraction of query-driven pagination states and
demonstrates bidirectional hook routing using coroutine generator boundaries.

Key Concepts:
- Functional Decoupling via Depends: Offloading request parameters mapping onto
  reusable external sub-routines, isolating endpoint logic from extraction mechanics.
- Inversion of Control Execution Flow: FastAPI intercepting route invocation to supply
  hydrated dictionary returns straight into runtime signature arguments.
- Yield Cleanup Boundaries: Constructing execution contexts that run entry setups,
  suspend at the yield junction for the handler, and predictably resume post-response.
"""

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
async def get_employees(
    pagination: dict[str, int] = Depends(pagination),
    session: None = Depends(security_session),
):
    return employees_db[pagination["skip"] : pagination["limit"] + pagination["skip"]]


if __name__ == "__main__":
    uvicorn.run("08_dependency_injection:app", reload=True)
