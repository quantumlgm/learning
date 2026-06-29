"""
Lesson 01: Creating a Minimal FastAPI Application

This script demonstrates the most basic configuration of a FastAPI server.
It includes a single REST API endpoint and demonstrates how to programmatically
launch the Uvicorn ASGI server with hot-reloading enabled.
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/", summary="General", tags=["General roots"])
def root():
    return "Hello world!"


if __name__ == "__main__":
    uvicorn.run("01_minimal_app:app", reload=True)
