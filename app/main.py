from fastapi import FastAPI
from utils import create_json
from utils import test_date


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/atcoder/upcoming_contests")
def fetch_contests():
    return create_json.get_contests_json()

@app.get("/atcoder/test1")
def fetch_test1():
    return test_date.fetch_not_start_time_json(test_date.not_start_time_json)

@app.get("/atcoder/test2")
def fetch_test1():
    return test_date.fetch_not_start_time_json(test_date.contest_type_json)

@app.get("/atcoder/test3")
def fetch_test1():
    return test_date.fetch_not_start_time_json(test_date.date_format_json)

@app.get("/atcoder/test4")
def fetch_test1():
    return test_date.fetch_not_start_time_json(test_date.date_cornercase)