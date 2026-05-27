from fastapi import FastAPI, HTTPException
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
    try:
        return {"reply": chat(req.message)}
    except RuntimeError as e:
        # Missing API key, etc. — return a clean message instead of a 500.
        raise HTTPException(status_code=503, detail=str(e))
