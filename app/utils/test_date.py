import json


def fetch_not_start_time_json(data):
    return json.loads(data)

not_start_time_json = [
  {
    "starttime": "2025-01-25 21:00:00+0900",
    "title": "AtCoder Beginner Contest 390",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "starttime": "2025-01-26 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "starttime": "2025-02-01 21:00:00+0900",
    "title": "AtCoder Beginner Contest 391",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "starttime": "2025-02-02 19:00:00+0900",
    "title": "AtCoder Heuristic Contest 042",
    "time": "04:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "starttime": "2025-02-08 21:00:00+0900",
    "title": "日本レジストリサービス（JPRS）プログラミングコンテスト2025#1（AtCoder Beginner Contest 392）",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  }
]


contest_type_json = [
  {
    "start_time": "2025-01-25 21:00:00+0900",
    "title": "AtCoder Beginner Contest 390",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-01-26 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "start_time": "2025-02-01 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 1)",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ARC"
  },
  {
    "start_time": "2025-02-02 19:00:00+0900",
    "title": "AtCoder Heuristic Contest 042",
    "time": "04:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "start_time": "2025-02-08 21:00:00+0900",
    "title": "AtCoder Grand Contest 098",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "AGC"
  }, 
  {
    "start_time": "2025-02-08 21:00:00+0900",
    "title": "Normal Contest",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": ""
  }
]


date_format_json = [
  {
    "start_time": "2025-01-25 21:00:00+0900",
    "title": "AtCoder Beginner Contest 390",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025/01/26 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "start_time": "2025-02 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 1)",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ARC"
  },
  {
    "start_time": "2025-02-02 19/00/00+0900",
    "title": "AtCoder Heuristic Contest 042",
    "time": "04:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "start_time": "2025-02-08 21:00:00+0900",
    "title": "AtCoder Grand Contest 098",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "AGC"
  }, 
  {
    "start_time": "2025-02-08 21:00:00+0900",
    "title": "Normal Contest",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": ""
  }
]

date_cornercase = [
  {
    "start_time": "2025-01-25 21:00:00+0900",
    "title": "AtCoder Beginner Contest 390",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-01-25 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "start_time": "2025-01-31 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "start_time": "2025-02-01 21:00:00+0900",
    "title": "AtCoder Beginner Contest 391",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-02-02 10:00:00+0900",
    "title": "AtCoder Heuristic Contest 042",
    "time": "04:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "start_time": "2025-02-02 19:00:00+0900",
    "title": "AtCoder Heuristic Contest 042",
    "time": "04:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "start_time": "2025-02-08 10:00:00+0900",
    "title": "日本レジストリサービス（JPRS）プログラミングコンテスト2025#1（AtCoder Beginner Contest 392）",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  }
  ]

trigger_test = [
  {
    "start_time": "2025-01-23 21:00:00+0900",
    "title": "AtCoder Beginner Contest 390",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-01-24 21:00:00+0900",
    "title": "AtCoder Regular Contest 191 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "start_time": "2025-01-25 21:00:00+0900",
    "title": "AtCoder Beginner Contest 391",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-01-26 19:00:00+0900",
    "title": "AtCoder Heuristic Contest 042",
    "time": "04:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "start_time": "2025-02-08 21:00:00+0900",
    "title": "日本レジストリサービス（JPRS）プログラミングコンテスト2025#1（AtCoder Beginner Contest 392）",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-02-09 21:00:00+0900",
    "title": "AtCoder Regular Contest 192 (Div. 2)",
    "time": "02:00",
    "rated_target": "1200 ~ 2399",
    "category": "ARC"
  },
  {
    "start_time": "2025-02-14 19:00:00+0900",
    "title": "RECRUIT 日本橋ハーフマラソン 2025冬（AtCoder Heuristic Contest 043）",
    "time": "240:00",
    "rated_target": "All",
    "category": "AHC"
  },
  {
    "start_time": "2025-02-15 21:00:00+0900",
    "title": "AtCoder Beginner Contest 393",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-02-22 21:00:00+0900",
    "title": "鹿島建設プログラミングコンテスト2025（AtCoder Beginner Contest 394）",
    "time": "01:40",
    "rated_target": "~ 1999",
    "category": "ABC"
  },
  {
    "start_time": "2025-03-02 13:00:00+0900",
    "title": "第二回マスターズ選手権-予選-",
    "time": "06:00",
    "rated_target": "-",
    "category": ""
  }
]

not_start_time_json = json.dumps(not_start_time_json, ensure_ascii=False, indent=2)
contest_type_json = json.dumps(contest_type_json, ensure_ascii=False, indent=2)
date_format_json = json.dumps(date_format_json, ensure_ascii=False, indent=2)
date_cornercase = json.dumps(date_cornercase, ensure_ascii=False, indent=2)
trigger_test = json.dumps(trigger_test, ensure_ascii=False, indent=2)