from pydantic import BaseModel


class Book(BaseModel):
    book_id: int
    title: str
    author: str
    genre: str
    isbn13: int
    publication_year: int
    price: float
    in_stock: bool
