from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os, json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_PATH = "backend/data"


def load_json(path):
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
    
@app.get("/topics")
def get_topics():
    data = load_json(f"{BASE_PATH}/topics.json")
    return {"topics": data["topics"]}


@app.get("/modules/{topic}/{level}")
def list_modules(topic: str, level: str):
    modules_path = f"{BASE_PATH}/{topic}/{level}/modules"
    if not os.path.isdir(modules_path):
        raise HTTPException(status_code=404, detail="Modules not found")

    modules = []
    for file in os.listdir(modules_path):
        if file.endswith(".json"):
            modules.append(file.replace(".json", ""))

    return {"modules": modules}


@app.get("/module/{topic}/{level}/{module_name}")
def get_module(topic: str, level: str, module_name: str):
    path = f"{BASE_PATH}/{topic}/{level}/modules/{module_name}.json"
    return load_json(path)


@app.get("/flashcards/{topic}/{level}")
def get_flashcards(topic: str, level: str):
    path = f"{BASE_PATH}/{topic}/{level}/flashcards.json"
    return load_json(path)


@app.get("/quizzes/{topic}/{level}")
def get_quizzes(topic: str, level: str):
    path = f"{BASE_PATH}/{topic}/{level}/quizzes.json"
    return load_json(path)
