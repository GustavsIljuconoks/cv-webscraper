import json
from collections import deque
import os
import datetime

HISTORY_FILE = "search_history.json"
MAX_HISTORY = 20

def load_search_history():
    if not os.path.exists(HISTORY_FILE):
        return deque([], maxlen=MAX_HISTORY)
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
            return deque(history, maxlen=MAX_HISTORY)
    except json.JSONDecodeError:
        return deque([], maxlen=MAX_HISTORY)

def save_search_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(list(history), f, indent=2, ensure_ascii=False, default=str)

def add_search_to_history(keywords, location, salary, jobs_count):
    history = load_search_history()
    search_entry = {
        "timestamp": datetime.date.today(),
        "keywords": keywords,
        "location": location,
        "salary": salary,
        "results": jobs_count
    }
    history.append(search_entry)
    save_search_history(history)
