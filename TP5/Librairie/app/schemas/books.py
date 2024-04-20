from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    id: str 
    name: str = Field(min_length=3, max_length=50)
    author: str
    editor :str
    price : int
    owner_id: str