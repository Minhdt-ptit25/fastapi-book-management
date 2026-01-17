from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str
    bio: str | None = None

class AuthorCreate(AuthorBase):
    """Schema for create author"""
    pass

class AuthorUpdate(AuthorBase):
    """Schema for update author"""

    name: str | None = None
    bio: str | None = None

class AuthorInDBBase(AuthorBase):
    id: int

    class Config:
        from_attributes = True #Pydantic read from SQLAlchemy model

class Author(AuthorInDBBase):
    """schema return for author"""
    pass 