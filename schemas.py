from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)
    password: str = Field(min_length=8, max_length=120)


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: str | None = None
    image_path: str


class PosttBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)


class PostCreate(PosttBase):
    user_id: int


class PostResponse(PosttBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: datetime
    author: UserResponse
