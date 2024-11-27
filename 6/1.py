# pip install fastapi uvicorn

from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 다른사람이 만든 걸 쓸 때에는
# object << 안에 뭐가 들어있는지 신경을 쓰지 않아도 된다.
# class에 어떠한 값이 들어가고, 어떠한 값이 나오는지만 알고 있으면 된다.


@app.get("/")
async def this_is_fastapi():
    return "hello world!"


# 이를 던더 혹은 매직메서드라고 부름. 던더(double underscore) 파이썬에서 미리 정해진 무언가.
# 내가 직접 실행시킨 코드가 __main__이라는 __name__을 가짐. __name__test 바탕으로 테스트
if __name__ == "__main__":
    uvicorn.run("1:app")
