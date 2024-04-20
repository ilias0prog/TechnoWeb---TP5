
from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy import func

from app.schemas.books import BookSchema
from app.database import Session
from app.models.book import Book 


def get_all_books() -> list[BookSchema]:
    with Session() as session:
        statement = select(Book)
        books_data = session.scalars(statement).all()
        return [
            Book(
                id=book.id,
                name=book.name,
                author=book.author,
                editor=book.editor
            )
            for book in books_data]
    
    
def get_amount_books() -> int:
    with Session() as session:
        nb = session.query(func.count(Book.id)).scalar()
    return nb

def check_input_validity(*args):
    """
    Checks the validity of input fields.

    Args:
        *args: Variable number of input fields to check.

    Raises:
        ValueError: If any of the input fields is empty or contains only spaces.

    Returns:
        None
    """
    for input in args:
        # Check if empty string :
        if len(input) < 1:
            raise ValueError("All the fields must be filled")
        # Check if only spacebars :
        i = input.strip()
        if len(i) < 1:
            raise ValueError("Please provide real title, author and editor")
    return

def get_book_by_id(book_id: str) -> BookSchema | None:
    """
    Retrieves a book from the bookstore by its ID.

    Args:
        book_id (str): The ID of the book to retrieve.

    Returns:
        Book | None: The book object if found, None otherwise.
    """
    with Session() as session:
        statement = select(Book).filter_by(id=book_id)
        book = session.scalar(statement) 
        if book is not None:
            return Book(
                id = book.id,
                name=book.name,
                author = book.author,
                editor = book.editor,
                price = book.price,
                owner_id = book.owner_id)
    return None

def save_book(new_book: BookSchema) -> BookSchema:
    """
    Saves a new book to the bookstore.

    Args:
        new_book (Book): The book object to save.

    Returns:
        Book: The saved book object.
    """
    with Session() as session:
        book = Book(id = new_book.id,
        name = new_book.name,
        author = new_book.author,
        editor = new_book.editor,
        price = new_book.price,
        owner_id = new_book.owner_id)
        session.add(book)
        session.commit()


def delete_book_data(book_id):
    """
    Deletes a book from the bookstore based on its ID.

    Args:
        book_id (str): The ID of the book to delete.

    Returns:
        None
    """
    with Session() as session:
        statement = select(Book).filter_by(id=book_id)
        user = session.scalars(statement).one()
        session.delete(user)
        session.commit()

def update_book_data(new_data: BookSchema) -> BookSchema | None:
    """
    Updates the fields of a book in the bookstore.

    Args:
        book_id (str): The ID of the book to update.
        updated_fields (dict): A dictionary containing the updated fields and their values.

    Returns:
        Book | None: The updated book object if found and updated successfully, None otherwise.
    """
    
    with Session() as session:
        statement = select(Book).filter_by(id = id)
        book = session.scalars(statement).one()
        book.name = new_data.name,
        book.author = new_data.author,
        book.editor = new_data.editor,
        book.price = new_data.price,
        book.owner_id = new_data.owner_id
        session.commit()
        return book
