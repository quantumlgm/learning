"""
Lesson 02: Building a Basic REST API for Book Management

This script demonstrates the core concepts of handling different HTTP methods
(GET and POST) using FastAPI. It implements a simple in-memory data store for
books, features parameterized path routing for retrieving specific records with
automatic type validation, utilizes Pydantic models for request body parsing,
and showcases structured error handling via HTTPException.
"""

from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()


books = [
    {"id": 1, "title": "Python Fastapi", "author": "Quantumlgm"},
    {"id": 2, "title": "PostgreSQL - Be better", "author": "Quantumlgm"},
]


@app.get("/books", tags=["Books"], summary="Get all the books")
def read_books():
    return books


@app.get("/books/{id}", tags=["Books"], summary="Get one of the all books")
def get_book(id: int):
    for b in books:
        if b["id"] == id:
            return b
    raise HTTPException(status_code=404, detail="The book wasn't found.")


class NewBook(BaseModel):
    title: str
    author: str


@app.post("/books", tags=["Books"])
def create_book(new_book: NewBook):
    books.append(
        {
            "id": len(books) + 1,
            "title": new_book.title,
            "author": new_book.author,
        }
    )
    return {"success": True}


if __name__ == "__main__":
    uvicorn.run("02_rest_api_books:app", reload=True)
