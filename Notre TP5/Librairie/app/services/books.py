
from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.schemas.books import Book
from app.database import Session
from app.models.book import Book


def get_all_books() -> list[Book]:
    with Session() as session:
        statement = select(Book)
        books_data = session.scalars(statement).unique().all()
        return [
            Book(
                id=book.id,
                name=book.name,
                author=book.author,
                editor=book.editor
            )
            for book in books_data
        ]