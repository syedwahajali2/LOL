import json
from pathlib import Path

MEMORY_FILE = Path("assistant_memory.json")

def load_memory():
    if not MEMORY_FILE.exists():
        return {}
    try:
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}

def save_memory(data):
    MEMORY_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

def remember(key, value):
    data = load_memory()
    data[str(key)] = str(value)
    save_memory(data)

def recall(key):
    return load_memory().get(str(key))
