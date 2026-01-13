from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# Usuário
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    items: List[ProductResponse] = []

    class Config:
        orm_mode = True

# Token JWT
class Token(BaseModel):
    access_token: str
    token_type: str