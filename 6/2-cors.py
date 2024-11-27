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

if __name__ == "__main__":
    uvicorn.run("2-cors:app")
