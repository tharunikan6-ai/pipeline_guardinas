import json
import os

DB_PATH = "history.json"

def save_healing_event(event_data: dict):
    """Persists every autonomous fix for the dashboard history."""
    history = []
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            history = json.load(f)
    
    history.append(event_data)
    
    with open(DB_PATH, "w") as f:
        json.dump(history, f, indent=4)

def get_history():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)