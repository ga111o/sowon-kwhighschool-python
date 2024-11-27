from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
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


@app.get("/add")
# async def add_numbers(num1, num2): << 타입 검사 안 할 땐 문자열로 받는다고 말하기
async def add_numbers(num1: int, num2: int):
    return num1 + num2

if __name__ == "__main__":
    uvicorn.run("3-url-parameter:app")
