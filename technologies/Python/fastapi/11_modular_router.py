"""
Lesson 11: Enterprise Architecture and Routing Modularization via APIRouter

This script delivers the final architectural refinement by decoupling route
registrations into specialized domain controllers using FastAPI's APIRouter.
The entry point handles application configuration and service bootstrapping.

Key Concepts:
- Domain-Driven Route Decoupling: Extracting endpoints into isolated sub-modules
  encapsulated by specific URL prefixes and OpenAPI identification tags.
- Distributed Application Merging: Consolidating multiple autonomous routers into
  a single monolithic routing table using the core 'include_router' pipeline.
- Scalable Structural Layouts: Mirroring production-ready directory trees where
  business logic, schemas, and initialization boundaries remain strictly separated.
"""

from fastapi import FastAPI
import uvicorn
from employees import employee_router

app = FastAPI()
app.include_router(
    employee_router,
)


if __name__ == "__main__":
    uvicorn.run("11_modular_router:app", reload=True)
