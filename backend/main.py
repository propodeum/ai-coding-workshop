from fastapi import FastAPI
from pydantic import BaseModel

from llm import chat

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, world!"}


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    return {"reply": chat(req.message)}
