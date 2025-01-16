import json
from utils.fetch_contests import fetch_contests

column = ["start_time", "title", "time", "rated_target", "category"]

def get_contests_json():

    contests_info = fetch_contests()

    contests_json = {}

    for id, contest in enumerate(contests_info):

        contest_json = {}
        for index, detail in enumerate(contest):
            contest_json[column[index]] = detail
        contests_json[id] = contest_json

    json_data = json.dumps(contests_json, ensure_ascii=False, indent=2)

    print(json_data)
    return json.loads(json_data)
