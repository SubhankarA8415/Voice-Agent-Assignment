import json
import os

SCHEME_FILE = os.path.join(os.path.dirname(__file__), "schemes.json")

def load_schemes():
    with open(SCHEME_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_all_schemes():
    return load_schemes()
