import aiohttp

from app.schemas.quiz import QuizRequests, QuizResponse

async def get_quiz(quiz: QuizRequests):
    url  = f"https://jservice.io/api/random?count={quiz.questions_num}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data_json = await response.json()
    print(data_json)
    list_quiz = []
    for i in data_json:
        list_quiz.append(QuizResponse(id_question=i["id"], text_question=i["question"],
        text_answer = i["answer"], date_create_question = i["created_at"]))
    print(list_quiz)
    return list_quiz