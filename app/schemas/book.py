from pydantic import BaseModel
from datetime import datetime

from app.schemas.author import Author
from app.schemas.category import Category



class BookBase(BaseModel):
    title: str
    description: str | None = None
    published_year: int | None = None
    category_id: int
    author_id: int

class BookCreate(BookBase):
    """Schema for create book"""
    pass 

class BookUpdate(BookBase):
    """Schema for update book"""
    name: str |None = None
    bio: str | None = None
    title: str | None = None
    description: str | None = None
    published_year: int | None = None
    category_id: int | None = None
    author_id: int | None = None

class BookInDBBase(BookBase):
    id: int
    title: str 
    description: str | None = None
    published_year: int 
    category_id: int
    author_id: int
    cover_image: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True #Pydantic read from sqlalchemy model

#schemas nested for author and category
class Book(BookInDBBase):
    author: Author
    category: Category

