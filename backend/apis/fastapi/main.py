from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def home():
    return "Welcome Home"
