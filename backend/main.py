from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import uvicorn
import json
from functions_on_db import get_categories_tables
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
        "items": ["Игрок1", "Игрок2", "Игрок3"], "color": "#e74c3c"},
    {"id": 1, "name": "Карандаш кассета", "items": [
        "Игрок1", "Игрок2"], "color": "#3498db"},
    {"id": 2, "name": "Домашний телефон", "items": [
        "Игрок1", "Игрок2"], "color": "#2ecc71"},
    {"id": 3, "name": "Словарь без инета", "items": [
        "Игрок1", "Игрок2"], "color": "#f1c40f"},
    {"id": 4, "name": "Старый комп VS Новый", "items": [
        "Игрок1", "Игрок2"], "color": "#9b59b6"},
    {"id": 5, "name": "Железный конструктор", "items": [
        "Игрок1", "Игрок2"], "color": "#e67e22"},
    {"id": 6, "name": "Перо VS ручка VS Граф.планшет",
        "items": ["Игрок1", "Игрок2"], "color": "#1abc9c"},
    {"id": 7, "name": "Перемотать ДВД", "items": [
        "Игрок1", "Игрок2"], "color": "#34495e"},
    {"id": 8, "name": "За рулём", "items": [
        "Игрок1", "Игрок2"], "color": "#f39c12"},
    {"id": 9, "name": "НТО", "items": [
        "Игрок1", "Игрок2"], "color": "#7f8c8d"},
]

LEADERS = [
    {"rank": 1, "name": "SMS-T", "category": "рекорд",
        "score": 123, "user_name": "Игрок 1"},
    {"rank": 2, "name": "Карандаш кассета",
        "category": "время (наименьшее)", "score": 45, "user_name": "Игрок 23"},
    {"rank": 3, "name": "Домашний телефон",
        "category": "время (наименьшее)", "score": 30, "user_name": "Игрок 10"},
    {"rank": 4, "name": "Словарь без инета",
        "category": "время (наименьшее)", "score": 25, "user_name": "Игрок 1"},
    {"rank": 5, "name": "Старый комп VS Новый",
        "category": "рекорд", "score": 110, "user_name": "Игрок 11"},
    {"rank": 6, "name": "Железный конструктор",
        "category": "время (наименьшее)", "score": 50, "user_name": "Игрок 9"},
    {"rank": 7, "name": "Перо VS ручка VS Граф.планшет",
        "category": "время (наименьшее)", "score": 35, "user_name": "Игрок 12"},
    {"rank": 8, "name": "Перемотать ДВД",
        "category": "время (наименьшее)", "score": 20, "user_name": "Игрок 1"},
    {"rank": 9, "name": "За рулём",
        "category": "время (наибольшее)", "score": 99, "user_name": "Игрок 1"},
    {"rank": 10, "name": "НТО",
        "category": "время (наименьшее)", "score": 15, "user_name": "Игрок 1"},
]

ESPORTS = {
    "categories": [
        {"id": 0, "name": "Гонки", "color": "#e74c3c"},
        {"id": 1, "name": "Пакман", "color": "#3498db"},
        {"id": 2, "name": "Fruit ninja", "color": "#2ecc71"},
        {"id": 3, "name": "Тетрис", "color": "#f1c40f"},
    ],
    "results": {
        0: [{"player": "Игрок1", "score": 12}, {"player": "Игрок2", "score": 15}],
        1: [{"player": "Игрок1", "score": 200}, {"player": "Игрок2", "score": 180}],
        2: [{"player": "Игрок1", "score": 350}, {"player": "Игрок2", "score": 330}],
        3: [{"player": "Игрок1", "score": 500}, {"player": "Игрок2", "score": 480}],
    }
}

# ===DATABASE=== FATALL ERROR НЕ НАДО ТАК

# === API ===


@app.get("/api/categories")
def get_categories():
    categories = get_categories_tables()
    # print(categories)
    return [{"id": c["id"], "name": c["name"], "color": c.get("color", "#fff")} for c in categories]


@app.get("/api/categories/{cat_id}/top10")
def get_category_top10(cat_id: int):
    categories = get_categories_tables()
    if cat_id < 0 or cat_id >= len(categories):
        raise HTTPException(status_code=404)
    cat = categories[cat_id]
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
