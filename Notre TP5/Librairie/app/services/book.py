from datetime import datetime

from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.schemas.books import Book
from app.database import Session
from app.models.book import Book


def get_all_books() -> list[Book]:
    