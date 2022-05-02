import datetime
from pydantic import BaseModel

class QuizRequests(BaseModel):
    questions_num: int

class QuizResponse(BaseModel):
    id_question: int
    text_question: str
    text_answer: str
    date_create_question: datetime.datetime