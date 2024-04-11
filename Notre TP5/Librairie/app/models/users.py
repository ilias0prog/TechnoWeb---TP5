from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    
    id          : Mapped[str] = mapped_column(String(72), primary_key=True)
    username    : Mapped[str] = mapped_column(String(72), unique=True)
    password    : Mapped[str] = mapped_column(String(72))
    email       : Mapped[str] = mapped_column(String(72), unique=True)
    firstname    : Mapped[str] = mapped_column(String(72))
    name    : Mapped[str] = mapped_column(String(72))
