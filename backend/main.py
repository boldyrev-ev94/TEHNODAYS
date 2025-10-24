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
            "Цой Алексей",
            "Кологривов Захар",
            "Копытова Елизавета ",
            "Тимофеева Наталья ",
            "Уваров Глеб ",
            "Попов Кирилл ",
            "Балеев Гриша",
            "Жданов Андрей",
            "Коробкейников Артём ",
            "Коростелева Варвара",


        ], "color": "#E4AFAF"},
    {"id": 1, "name": "Карандаш кассета",
        "items": [
            "Квацабая Александр ",
            "Ибрагимова Светлана ",
            "Ломанкова Юлия",
            "Кузнецова Вероника",
            "Галимова Светлана ",


        ], "color": "#3498db"},
    {"id": 2, "name": "Домашний телефон",
        "items": [
            "Кологривов Захар",
            "Копытова Елизавета ",
            "Новикова Светлана ",


        ], "color": "#2ecc71"},
    {"id": 3, "name": "Словарь без инета",
        "items": [
            "Галимова Галина ",
            "Довыденко Данил",
            "стоарцев Артём ",
            "Рахимбеков Сергей",
            "Копытова Елизавета ",
            "Володин Владимир",
            "Кузнецова ",
            "Нигодин Роман",
            "Новикова Светлана ",
            "Джумаев Максим",



        ], "color": "#f1c40f"},
    {"id": 4, "name": "Старый комп VS Новый",
        "items": [
            "Копытова Елизавета ",
            "Дементьева Ольга",
            "Копытова Елизавета ",
            "Новикова Светлана ",
            "Яськов Михаил",
            "Решетников Артур ",
            "Джумаев Максим",
            "Четвергов Дмитрий"



        ], "color": "#9b59b6"},
    {"id": 5, "name": "Железный конструктор",
        "items": [
            ""
        ], "color": "#e67e22"},
    {"id": 6, "name": "Перо VS ручка VS Граф.планшет",
        "items": [
            ""
        ], "color": "#1abc9c"},
    {"id": 7, "name": "Перемотать ДВД",
        "items": [
            ""
        ], "color": "#34495e"},
    {"id": 8, "name": "За рулём",
        "items": [
            "Трапезников Клементьев максим Сергеевич ",
            "Копытова Елизавета ",
            "Медвеев Рома",
            "Емельянов Данил ",
            "Илья Подгорнов ",
            "Азаренко Эльвира ",
            "Мухутдинов Юрий ",
            "стоарцев Артём ",
            "Фишер Аркадий ",
            "Татаринцев Михаил",



        ], "color": "#f39c12"},
    {"id": 9, "name": "НТО",
        "items": [
            "Бойков Артём",
            "Коркина Варвара",
            "Рахимбеков Сергей",


        ], "color": "#7f8c8d"},
]

LEADERS = [
    {"rank": 1,
     "name": "SMS-T",
     "category": "Уваров Глеб ",
     "score":  "",
     "user_name": ""},
    {"rank": 2,
     "name": "Карандаш кассета",
     "category": "Квацабая Александр ",
     "score":  "",
     "user_name": ""},
    {"rank": 3,
     "name": "Домашний телефон",
     "category": "Кологривов Захар",
     "score":  "",
     "user_name": ""},
    {"rank": 4,
     "name": "Словарь без инета",
     "category": "Белов Артем ",
     "score":  "",
     "user_name": ""},
    {"rank": 5,
     "name": "Старый комп VS Новый",
     "category": "Копытова Елизавета",
     "score":  "",
     "user_name": ""},
    {"rank": 6,
     "name": "Железный конструктор",
     "category": "",
     "score":  "",
     "user_name": ""},
    {"rank": 7,
     "name": "Перо VS ручка VS Граф.планшет",
        "category": "Дементьева  Ольга",
        "score":  "",
        "user_name": ""},
    {"rank": 8,
     "name": "Перемотать ДВД",
        "category": "",
        "score":  "",
        "user_name": ""},
    {"rank": 9,
     "name": "За рулём",
     "category": "Трапезников  Клементьев",
     "score":  "",
     "user_name": ""},
    {"rank": 10,
     "name": "НТО",
        "category": "Коркина Варвара",
        "score": "",
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
        0: [
            {"player": "Михайлов Алексей", "score": "1:30"},
            # {"player": "Дорофеева София", "score": "1:35"},
            # {"player": "Балашев Александр ", "score": "2:05"},
            # {"player": "Венгуро Тимофей", "score": "2:10"}
        ],
        1: [
            {"player": "Лованкова Юлия", "score": 2750}
        ],
        2: [
            {"player": "", "score": 350}
        ],
        3: [
            {"player": "Скулов Никита", "score": 104638},
            # {"player": "Володин Владимир", "score": 1950},
            # {"player": "Рудман Софья", "score": 1950},
            # {"player": "Дутнефтер Русалина", "score": 1950}

        ],
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
