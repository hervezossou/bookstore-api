import json


def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def save_book_to_json(books, book_path):
    file = load_json_data(file_path=book_path)
    json.dump(books, file, indent=2)


def find_book_by_id(books, book_id):
    for book in books:
        if book.book_id == book_id:
            return book
    return None


def find_book_by_author(books, author):
    for book in books:
        if book.author == author:
            return book
    return None


def filter_book_by_author(books, author):
    booksFilteredByAuthor = []
    for book in books:
        if book.author == author:
            booksFilteredByAuthor.append(book)
    return booksFilteredByAuthor


def find_book_by_title(books, title):
    for book in books:
        if book.title == title:
            return book
    return None


def find_book_by_genre(books, genre):
    for book in books:
        if book.genre == genre:
            return book
    return None


def filter_book_by_genre(books, genre):
    booksFilteredByGenre = []
    for book in books:
        if book.genre == genre:
            booksFilteredByGenre.append(book)
    return booksFilteredByGenre
