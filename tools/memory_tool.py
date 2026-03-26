import json
import os

MEMORY_FILE = "data/memory.json"


def _load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def _save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def log_decision(email, decision):
    data = _load_memory()

    data.append(
        {
            "email_id": email.get("id"),
            "subject": email.get("subject"),
            "body": email.get("body"),
            "decision": decision,
        }
    )

    _save_memory(data)


def get_low_confidence(threshold=0.5):
    data = _load_memory()

    return [item for item in data if item["decision"].get("confidence", 1) < threshold]
