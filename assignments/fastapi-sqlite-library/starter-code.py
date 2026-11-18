import sqlite3

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

DATABASE_PATH = "books.db"

app = FastAPI(title="Books API")


class BookFields(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int


class Book(BookFields):
    id: int


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    try:
        # TODO: Create the books table if it does not exist.
        connection.commit()
    finally:
        connection.close()


initialize_database()


@app.get("/books", response_model=list[Book])
def list_books():
    connection = get_connection()
    try:
        # TODO: Read all books from SQLite and convert each row to a Book.
        return []
    finally:
        connection.close()


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    connection = get_connection()
    try:
        # TODO: Read one book or raise HTTPException with status 404.
        raise HTTPException(status_code=404, detail="Book not found")
    finally:
        connection.close()


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_fields: BookFields):
    connection = get_connection()
    try:
        # TODO: Insert the book, then return it with its generated id.
        raise HTTPException(status_code=501, detail="Not implemented")
    finally:
        connection.close()


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_fields: BookFields):
    connection = get_connection()
    try:
        # TODO: Update an existing book or raise HTTPException with status 404.
        raise HTTPException(status_code=501, detail="Not implemented")
    finally:
        connection.close()


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    connection = get_connection()
    try:
        # TODO: Delete an existing book or raise HTTPException with status 404.
        return Response(status_code=204)
    finally:
        connection.close()
