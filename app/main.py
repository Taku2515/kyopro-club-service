from fastapi import FastAPI
from utils import create_json


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fetch")
def fetch_root():
    return create_json.get_contests_json()