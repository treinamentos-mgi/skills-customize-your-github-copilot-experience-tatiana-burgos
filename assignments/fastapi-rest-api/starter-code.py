from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookFields(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int


class Book(BookFields):
    id: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books in the collection.
    return []


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Find the requested book or raise HTTPException with status 404.
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book_fields: BookFields):
    global next_book_id

    # TODO: Create a Book with the next id, store it, and return it.
    raise HTTPException(status_code=501, detail="Not implemented")


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_fields: BookFields):
    # TODO: Replace the book fields or raise HTTPException with status 404.
    raise HTTPException(status_code=501, detail="Not implemented")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    # TODO: Delete the book or raise HTTPException with status 404.
    raise HTTPException(status_code=501, detail="Not implemented")