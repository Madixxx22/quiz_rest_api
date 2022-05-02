import aiohttp
from fastapi import HTTPException

from app.db.crud_quiz import quiz_crud
from app.schemas.quiz import QuizRequests, QuizResponse


async def request_quiz(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data_json = await response.json()

    return data_json


async def get_quiz(quiz: QuizRequests) -> QuizResponse:
    url  = f"https://jservice.io/api/random?count={quiz.questions_num}"

    result = await quiz_crud.get_question()
    quiz_in_db = await quiz_crud.get_id()
    check = True

    while check:
        request = await request_quiz(url)
        for i in request:
            if i["id"] not in quiz_in_db:
                check = False

    for i in request:
        try:        
            quiz = QuizResponse(id_question=i["id"], text_question=i["question"],
            text_answer = i["answer"], date_create_question = i["created_at"])
            await quiz_crud.create_question(quiz)
        except:
            raise HTTPException(status_code=400, detail="Ошибка добавления в БД")

    if result is None:
        return {}
    else:
        return QuizResponse(id_question=result["id_question"], text_question=result["text_question"],
                    text_answer=result["text_answer"], date_create_question=result["date_create_question"])