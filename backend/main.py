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
"Кушнир Александр ",
"Пивоварова Нелли",
"Осина Анна",
"Яжена  Евгения",
"Бахтеев Тимофей",
"Утюжников Тиртха ",
"Фоменко Дима",
"Гудежников Миша",
"Руденко Любовь",
"Щип  Марина",






        ], "color": "#E4AFAF"},
    {"id": 1, "name": "Карандаш кассета",
        "items": [
            ""
            # "Квацабая Александр",
            # "Ибрагимова Светлана",
            # "Ломанкова Юлия",
            # "Кузнецова Вероника",
            # "Галимова Светлана",


        ], "color": "#3498db"},
    {"id": 2, "name": "Домашний телефон",
        "items": [
"Бекмухаметова  Елена",
"Головина  Оксана ",
"Артемьева Ананстасия ",
"Бахтеев Тимофей",
"Таценко дмитрий ",
"Звегенцев  Денис",
"Калинв  Наиль ",
"Конваленко Валерия",
"Овчинников  Геогргий",
"Артемьев Станислав",





        ], "color": "#2ecc71"},
    {"id": 3, "name": "Словарь без инета",
        "items": [
            "Головина Оксана",
"корчагов  Ярослав ",
"Иванюк Валерия ",
"Кондратюк Ярослав ",
"Никайлин Алексей",
"Лессина Элина",
"Калиев  Давид ",


            # "Решетников Артур ",
            # "Белов Артем ",
            # "Яськов Михаил ",
            # "Эльвира Азаренко",
            # "Фишер Аркадий ",
            # "Тюмин Алексей ",
            # "Джумаев Максим",
            # "Ульянов Артём",
            # "Новикова Светлана ",
            # "Эльдар Мустафин",






        ], "color": "#f1c40f"},
    {"id": 4, "name": "Старый комп VS Новый",
        "items": [
            "Ломахин Андрей "

            # "Решетников Артур ",
            # "Джумаев Максим",
            # "Ульянов Артём",
            # "Четвергов Дмитрий",
            # "П Ирина",
            # "Андреева Анна ",
            # "Потрикеев Дмитрий ",
            # "Кузнецова Елизавета",
            # "Петров Илья",
            # "Тютиков Костя",






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
"Кондратюк Ярослав ",
"Никалин Дмитрий",
" Пивоваров Дима",
"Флоленко  Паша",
"Вербитский дима",
"Кушнир Александр ",
"Копытова Елизавета",
"Оклей Данил",
"Артемьева Алиса",
"Утюжников Тиртха ",

        ], "color": "#f39c12"},
    {"id": 9, "name": "НТО",
        "items": [
            # "Бойков Артём",
            # "Коркина Варвара",
            # "Васильев Владислав",
            # "Рахимбеков Сергей",



        ], "color": "#7f8c8d"},
]

LEADERS = [
    {"rank": 1,
     "name": "SMS-T",
     "category": "Кушнир Александр ",
     "score":  "",
     "user_name": ""},
    {"rank": 2,
     "name": "Галимова Светлана ",
     "category":  "",
     "score":  "",
     "user_name": ""},
    {"rank": 3,
     "name": "Домашний телефон",
     "category": "Бекмухаметова  Елена",
     "score":  "",
     "user_name": ""},
    {"rank": 4,
     "name": "Словарь без инета",
     "category": "Головина Оксана",
     "score":  "",
     "user_name": ""},
    {"rank": 5,
     "name": "Старый комп VS Новый",
     "category": "Ломахин Андрей ",
     "score":  "",
     "user_name": ""},
    {"rank": 6,
     "name": "Железный конструктор",
     "category": "",
     "score":  "",
     "user_name": ""},
    {"rank": 7,
     "name": "Перо VS ручка VS Граф.планшет",
        "category": "",
        "score":  "",
        "user_name": ""},
    {"rank": 8,
     "name": "Перемотать ДВД",
        "category": "",
        "score":  "",
        "user_name": ""},
    {"rank": 9,
     "name": "За рулём",
     "category": "Кондратюк Ярослав ",
     "score":  "",
     "user_name": ""},
    {"rank": 10,
     "name": "НТО",
        "category": "",
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
            {"name": "Гонки", "player": "", "score": ""},
            {"name": "Гонки", "player": "", "score": ""},
            {"name": "Гонки", "player": "", "score": ""},
        ],
        1: [
            {"name": "Пакман", "player": "", "score": ""},
            {"name": "Пакман", "player": "", "score": ""},
            {"name": "Пакман", "player": "", "score": ""}
        ],
        2: [
            {"name": "Fruit ninja", "player": "", "score": ""},
            {"name": "Fruit ninja", "player": "", "score": ""},
            {"name": "Fruit ninja", "player": "", "score": ""}
        ],
        3: [
            {"name": "Тетрис", "player": "", "score": ""},
            {"name": "Тетрис", "player": "", "score": ""},
            {"name": "Тетрис", "player": "", "score": ""},
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
