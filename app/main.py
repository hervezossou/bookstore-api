from fastapi import FastAPI
from .models import Book
from .utils import (
    load_json_data,
    find_book_by_id,
    find_book_by_author,
    find_book_by_genre
)

app = FastAPI()


# Loading data from our JSON file
BASE_DIR = "data/books.json"
BOOKS_DATA = load_json_data(file_path=BASE_DIR)

books = [Book(**book_data) for book_data in BOOKS_DATA]

# Base route


@app.get("/books")
def get_books():
    return {"message": "Use specific search endpoints like /books/title or"
            + " /books/id"}


@app.get("/books/{id}")
def get_book_by_id(id: int):
    researched_book = find_book_by_id(books=books, book_id=id)
    if researched_book:
        return researched_book
    else:
        return {"message": "Book not found"}, 404


@app.get("/books/author/{author}")
def get_book_by_author(author: str):
    researched_book = find_book_by_author(books=books, author=author)
    if researched_book:
        return researched_book
    else:
        return {"message": "Book not found"}, 404


@app.get("/books/genre/{genre}")
def get_book_by_genre(genre: str):
    researched_book = find_book_by_genre(books=books, genre=genre)
    if researched_book:
        return researched_book
    else:
        return {"message": "Book not found"}, 404
