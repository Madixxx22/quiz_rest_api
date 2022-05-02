from fastapi import Body, FastAPI

from app.utils import get_quiz
from app.db.base import database
from app.schemas.quiz import QuizRequests, QuizResponse

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

@app.post("/quiz")
async def quiz(quiz_num: QuizRequests = Body(..., example = {"questions_num": 1})):
    return await get_quiz(quiz_num)