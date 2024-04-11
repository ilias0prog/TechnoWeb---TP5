from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: str
    message: str
