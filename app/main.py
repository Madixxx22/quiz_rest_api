from fastapi import FastAPI

from db.base import database, metadata, engine
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect() 

@app.get("/")
async def test():
    return {"Result": "success"}