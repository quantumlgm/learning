"""
Lesson 01: Creating a Minimal FastAPI Application

This script demonstrates the most basic configuration of a FastAPI server.
It includes a single REST API endpoint and demonstrates how to programmatically
launch the Uvicorn ASGI server with hot-reloading enabled.

Key Concepts:
- FastAPI Instance: Initializing the core application object which acts as the 
  central router and ASGI application interface.
- Path Operation Decorator: Using '@app.get("/")' to bind an HTTP GET request 
  on the root path to a specific Python function.
- OpenAPI Metadata: Leveraging 'summary' and 'tags' parameters within the 
  decorator to structure and document endpoints in the auto-generated Swagger UI.
- Programmatic ASGI Execution: Utilizing 'uvicorn.run()' inside the standard 
  Python main block to trigger hot-reloading without external CLI flags.
"""

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/", summary="General", tags=["General roots"])
def root():
    return "Hello world!"


if __name__ == "__main__":
    uvicorn.run("01_minimal_app:app", reload=True)
