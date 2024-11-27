from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def this_is_fastapi():
    return "hello world!"


class Message(BaseModel):
    content: str

# pydantic <<<< 타입 검사
# BaseModel <<<< 데이터 모델 정의


@app.post("/message")
async def create_message(message: Message):
    with open("./content.txt", "w") as f:
        f.write(message.content)
    return {"message": "저장되었습니다"}


if __name__ == "__main__":
    uvicorn.run("4-post:app")
