from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import hashlib
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://79.141.77.117"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CATEGORIES = [
    {"name": "Фрукты", "items": ["Яблоко", "Банан",
                                 "Апельсин", "Киви"], "color": "#e74c3c"},
    {"name": "Животные", "items": [
        "Кошка", "Собака", "Лиса", "Слон"], "color": "#3498db"},
    {"name": "Страны", "items": ["Россия", "Япония",
                                 "Франция", "Бразилия"], "color": "#2ecc71"},
    {"name": "Языки программирования", "items": [
        "Python", "JavaScript", "C++", "Rust"], "color": "#f1c40f"},
]


def get_hash(cat):
    data = json.dumps(cat, sort_keys=True, ensure_ascii=False)
    return hashlib.md5(data.encode('utf-8')).hexdigest()


@app.get("/categories")
def get_categories():
    return [{"name": c["name"], "color": c.get("color", "#fff")} for c in CATEGORIES]


@app.get("/categories/{idx}")
def get_category(idx: int, check: bool = False, etag: str = None):
    if idx < 0 or idx >= len(CATEGORIES):
        raise HTTPException(status_code=404)
    cat = CATEGORIES[idx]
    h = get_hash(cat)
    if check and etag == h:
        return {"notModified": True, "etag": h}
    return {**cat, "etag": h}


if __name__ == "main":
    uvicorn.run(app, host="79.141.77.117", port=8000)
