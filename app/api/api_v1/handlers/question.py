from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.models.question_model import Question
from app.models.user_model import User
from app.api.deps.user_deps import get_current_user
from app.schemas.question_schema import QuestionOut, QuestionCreate, QuestionUpdate
from app.services.question_service import QuestionService


question_router = APIRouter()

@question_router.get('/', summary="Get all questions of the user ", response_model=List[QuestionOut])
async def list(current_user: User = Depends(get_current_user)):
    return await QuestionService.list_questions(current_user)

@question_router.get('/search/{titre}', summary="Get all search questions", response_model=List[QuestionOut])
async def list(titre: str, current_user: User = Depends(get_current_user)):
    return await QuestionService.retrieve_question_by_titre(current_user, titre)

@question_router.post('/create', summary="Create Question", response_model=Question)
async def create_question(data: QuestionCreate, current_user: User = Depends(get_current_user)):
    return await QuestionService.create_question(current_user, data)


@question_router.get('/{question_id}', summary="Get question by question_id", response_model=QuestionOut)
async def retrieve(question_id: UUID, current_user: User = Depends(get_current_user)):
    return await QuestionService.retrieve_question(current_user, question_id)


@question_router.put('/{question_id}', summary="Update question by question_id", response_model=QuestionOut)
async def update(question_id: UUID, data: QuestionUpdate, current_user: User= Depends(get_current_user)):
    return await QuestionService.update_question(current_user, question_id, data)


@question_router.delete('/{question_id}', summary="Delete question by question_id")
async def delete(question_id: UUID, current_user: User = Depends(get_current_user)):
    await QuestionService.delete_question(current_user, question_id)
    return None