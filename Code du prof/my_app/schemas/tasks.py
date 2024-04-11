from datetime import datetime

from pydantic import BaseModel, Field

from my_app.schemas.comments import CommentSchema


class TaskSchema(BaseModel):
    id: str
    name: str = Field(min_length=3, max_length=50)
    description: str | None
    creation_date: datetime
    comments: list[CommentSchema] = []
    


class NewTaskSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str | None
