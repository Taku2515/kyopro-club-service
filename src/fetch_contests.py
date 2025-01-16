import requests
from bs4 import BeautifulSoup

CATEGORY = {
    "AtCoder Beginner Contest": True, 
    "AtCoder Regular Contest": True, 
    "AtCoder Grand Contest": True, 
    "AtCoder Heuristic Contest": True
}

short_category = {
    "AtCoder Beginner Contest": "ABC", 
    "AtCoder Regular Contest": "ARC", 
    "AtCoder Grand Contest": "AGC", 
    "AtCoder Heuristic Contest": "AHC"
}

URL = "https://atcoder.jp/contests/?lang=ja"

def fetch_contests():

    req = requests.get(URL)

    # サイト情報の取得
    bsObj = BeautifulSoup(req.content, "html.parser")

    # 予定されたコンテストのhtmlの取得
    contests_html = bsObj.find(id="contest-table-upcoming").find("tbody").find_all("tr")

    # [開催時刻, コンテスト名, 時間, rated対象, コンテストリンク, A(B|R|G|H)C]
    contests_info = [["" for i in range(5)] for j in range(len(contests_html))]

    # 予定されたコンテストをcontests_infoに代入
    for table_index, contest_html in enumerate(contests_html):

        contest_info = contest_html.find_all("td")

        for info_id, detail in enumerate(contest_info):

            contests_info[table_index][info_id] = detail.get_text().strip()

    # 不揃いな文字列の成形
    for table_index, contest_info in enumerate(contests_info):
        contests_info[table_index][1] = contest_info[1][4:]


    for table_index, contest_info in enumerate(contests_info):
        for contest_category in CATEGORY:

            if(contest_category in contest_info[1] and CATEGORY[contest_category]):
                contests_info[table_index][4] = short_category[contest_category]

    return contests_info