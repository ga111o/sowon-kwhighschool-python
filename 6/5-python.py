from fastapi import FastAPI
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/menu/{date}")
async def get_menu(date: str):
    with open("./menu.json", "r", encoding="utf-8") as f:
        menu_data = json.load(f)
    return menu_data.get("menu", {}).get(date, "메뉴가 없어요.")


if __name__ == "__main__":
    uvicorn.run("5-python:app", host="0.0.0.0", port=8085)
