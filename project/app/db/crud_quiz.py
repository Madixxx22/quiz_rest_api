import sqlalchemy

from .base import database
from app.models.quiz import quiz_question
from app.schemas.quiz import QuizResponse

#Класс работы с БД
class QuizCrud():
    async def create_question(self, quiz: QuizResponse):
        """Создание вопроса из викторины в БД"""
        query = quiz_question.insert().values(id_question = quiz.id_question, text_question = quiz.text_question,
            text_answer = quiz.text_answer, date_create_question = quiz.date_create_question)
        return await database.execute(query)

    async def get_question(self):
        """Получение последнего вопроса в БД"""
        query = quiz_question.select().order_by(sqlalchemy.desc(quiz_question.c.id)).limit(1)
        return await database.fetch_one(query)

    async def get_id(self):
        """Получение списка всех id вопросов"""
        query = sqlalchemy.select(quiz_question.c.id_question)
        return await database.fetch_all(query)

quiz_crud = QuizCrud()