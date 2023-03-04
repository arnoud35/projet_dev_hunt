from typing import List
from uuid import UUID
from app.models.user_model import User
from app.models.question_model import Question
from app.schemas.question_schema import QuestionCreate, QuestionUpdate

class QuestionService:
    @staticmethod
    async def list_questions(user: User) -> List[Question]:
        questions = await Question.find(Question.owner.id == user.id).to_list()
        return questions
    
    @staticmethod
    async def create_question(user: User, data: QuestionCreate) -> Question:
        question = Question(**data.dict(), owner=user)
        return await question.insert()

    @staticmethod
    async def retrieve_question(current_user: User, question_id: UUID):
        question = await Question.find_one(Question.question_id == question_id, Question.owner.id == current_user.id)
        return question
    # recherche par titre
    @staticmethod
    async def retrieve_question_by_titre(current_user: User, titre: str) -> List[Question]:
        question = await Question.find({"$or" : [{Question.titre : {"$regex" : titre}}, {Question.description : {"$regex" : titre}}]}).to_list()
        return question

    @staticmethod
    async def update_question(current_user: User, question_id: UUID, data: QuestionUpdate):
        question = await QuestionService.retrieve_question(current_user, question_id)
        await question.update({"$set" : data.dict(exclude_unset=True)})

        await question.save()
        return question

    @staticmethod
    async def delete_question(current_user: User, question_id: UUID):
        question = await QuestionService.retrieve_question(current_user, question_id)
        if question:
            await question.delete()
        return None        