from pydantic import BaseModel,Field


class UserSchema(BaseModel):
    id: str
    username: str
    firstname: str
    name: str
    email: str
    password: str = Field(min_length=8, max_length=20)
