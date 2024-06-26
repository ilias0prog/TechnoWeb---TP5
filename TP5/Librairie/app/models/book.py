from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer , ForeignKey

from app.database import Base


class Book(Base):
    __tablename__ = "books"
    
    id = mapped_column(String(72), primary_key=True)
    name = mapped_column(String(128))
    author = mapped_column(String(128))
    editor = mapped_column(String(72))
    price = mapped_column(Integer)
    owner_id = mapped_column(String(72), ForeignKey("users.id"))
      

