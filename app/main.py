from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test():
    return {"Result": "success"}