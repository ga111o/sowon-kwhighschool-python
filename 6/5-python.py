from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()


@app.get("/menu/{date}")
async def get_menu(date: str):
    with open("./menu.json", "r", encoding="utf-8") as f:
        menu_data = json.load(f)
    return menu_data.get("menu", {}).get(date, "메뉴가 없어요.")


if __name__ == "__main__":
    uvicorn.run("5-python:app")
