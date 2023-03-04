from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    matricule: str = Field(..., min_length=5, max_length=10, description="user matricule")
    role: int
    password: str = Field(...,min_length=8, max_length=24, description="user password")
    first_name: str = Field(...,min_length=2, max_length=55, description="user first_name")
    last_name: str = Field(...,min_length=2, max_length=55, description="user last_name")

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(..., title='Title', max_length=55, min_length=2)
    last_name: Optional[str] = Field(..., title='Title', max_length=55, min_length=2)

class UserOut(BaseModel):
    user_id: UUID
    matricule: str
    email: EmailStr
    role: int
    first_name: str
    last_name: str
