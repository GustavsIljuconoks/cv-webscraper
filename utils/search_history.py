import json
from collections import deque
import os

HISTORY_FILE = "search_history.json"
MAX_HISTORY = 20  

def load_search_history():
    if not os.path.exists(HISTORY_FILE):
        return deque([], maxlen=MAX_HISTORY)
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
        return deque(history, maxlen=MAX_HISTORY)

def save_search_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(list(history), f, indent=2)

def add_search_to_history(keywords, location, salary):
    history = load_search_history()
    search_entry = {
        "keywords": keywords,
        "location": location,
        "salary": salary
    }
    history.append(search_entry)
    save_search_history(history)
