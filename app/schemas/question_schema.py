from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

class QuestionCreate(BaseModel):
    titre: str = Field(..., title='Title', max_length=100, min_length=10)
    description: str
    reponse: bool

class QuestionUpdate(BaseModel):
    titre: str = Field(..., title='Title', max_length=100, min_length=10)
    description: str
    reponse: bool

class QuestionOut(BaseModel):
    question_id: UUID
    titre: str
    description: str
    reponse: bool
    created_at : datetime 
    updated_at : datetime 
