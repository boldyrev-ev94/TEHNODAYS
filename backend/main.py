from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import uvicorn
import json
# from functions_on_db import get_categories_tables
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
        "http://79.141.77.117"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# === Данные ===
CATEGORIES = [
    {"id": 0, "name": "SMS-T",
        "items": [
            "Цой Александр","Тимофеевна Наталья", "Уваров Глеб", "Попов Кирилл", "Балеев Гриша", "Копытова Елизавета", "Кологривов Захар","Жданов Андрей", "Коростелева Варвара"
            ], "color": "#E4AFAF"},
    {"id": 1, "name": "Карандаш кассета", "items": [
        ""
        ], "color": "#3498db"},
    {"id": 2, "name": "Домашний телефон", "items": [
        "Копытова Елизавета", "Новикова  Светлана", "Кологривов Захар", "Белов Артем "
        ], "color": "#2ecc71"},
    {"id": 3, "name": "Словарь без инета", "items": [
        "Копытова  Елизавета", "Новикова Светлана", "Эльдар Мустафин"
        ], "color": "#f1c40f"},
    {"id": 4, "name": "Старый комп VS Новый", "items": [
        "Ольга Демьентева", "Копытова Елизавета ", "Копытова  Елизавета ", "Новикова  Светлана ", "Яськов  Михаил"
        ], "color": "#9b59b6"},
    {"id": 5, "name": "Железный конструктор", "items": [
        ""
        ], "color": "#e67e22"},
    {"id": 6, "name": "Перо VS ручка VS Граф.планшет",
        "items": [
            ""
            ], "color": "#1abc9c"},
    {"id": 7, "name": "Перемотать ДВД", "items": [
        ""
        ], "color": "#34495e"},
    {"id": 8, "name": "За рулём", "items": [
        "Копытова Елизавета ", "Медвеев Рома" ,"Трапезников  Клементьев максим Сергеевич "
        ], "color": "#f39c12"},
    {"id": 9, "name": "НТО", "items": [
        ""
        ], "color": "#7f8c8d"},
]

LEADERS = [
    {"rank": 1, 
     "name": "SMS-T", 
     "category": "Цой Александр",
     "score": 3, 
     "user_name": ""},
    {"rank": 2, 
     "name": "Карандаш кассета",     
     "category": "",
     "score": 0, 
     "user_name": ""},
    {"rank": 3,
     "name": "Домашний телефон",
     "category": "Копытова Елизавета", 
     "score": 2, 
     "user_name": ""},
    {"rank": 4,
     "name": "Словарь без инета",
     "category": "Копытова Елизавета",
     "score": 3,
     "user_name": ""},
    {"rank": 5,
     "name": "Старый комп VS Новый",
    "category": "Копытова Елизавета",
    "score": 2,
    "user_name": ""},
    {"rank": 6, 
     "name": "Железный конструктор",
        "category": "",
        "score": 0,
        "user_name": ""},
    {"rank": 7,
     "name": "Перо VS ручка VS Граф.планшет",
        "category": "Дементьева  Ольга",
        "score": 0,
        "user_name": ""},
    {"rank": 8,
     "name": "Перемотать ДВД",
        "category": "",
        "score": 0,
        "user_name": ""},
    {"rank": 9,
     "name": "За рулём",
     "category":"Медвеев Рома",
     "score": 0,
     "user_name": ""},
    {"rank": 10,
     "name": "НТО",
        "category": "",
        "score": 0,
        "user_name": ""},
]

ESPORTS = {
    "categories": [
        {"id": 0, "name": "Гонки", "color": "#e74c3c"},
        {"id": 1, "name": "Пакман", "color": "#3498db"},
        {"id": 2, "name": "Fruit ninja", "color": "#2ecc71"},
        {"id": 3, "name": "Тетрис", "color": "#f1c40f"},
    ],
    "results": {
        0: [{"player": "", "score": 12}],
        1: [{"player": "", "score": 200}],
        2: [{"player": "", "score": 350}],
        3: [{"player": "", "score": 500}],
    }
}

# ===DATABASE=== FATALL ERROR НЕ НАДО ТАК

# === API ===


@app.get("/api/categories")
def get_categories():
    # categories = get_categories_tables()
    # print(categories)
    return [{"id": c["id"], "name": c["name"], "color": c.get("color", "#fff")} for c in CATEGORIES]


@app.get("/api/categories/{cat_id}/top10")
def get_category_top10(cat_id: int):
    # categories = get_categories_tables()
    if cat_id < 0 or cat_id >= len(CATEGORIES):
        raise HTTPException(status_code=404)
    cat = CATEGORIES[cat_id]
    return [{"name": name, "score": idx+1} for idx, name in enumerate(cat["items"])]


@app.get("/api/leaders")
def get_leaders():

    return LEADERS


@app.get("/api/esports")
def get_esports():
    return ESPORTS


@app.get("/api/esports/{cat_id}/top10")
def get_esports_top10(cat_id: int):
    if cat_id not in ESPORTS["results"]:
        raise HTTPException(status_code=404)
    return ESPORTS["results"][cat_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
