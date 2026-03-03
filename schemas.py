from audioop import minmax
from pydantic import BaseModel, ConfigDict, Field

class PosttBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

class PostCreate(PosttBase):
    pass

class PostResponse(PosttBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
    
