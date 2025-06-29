import json

with open('patterns_list.json', encoding='utf-8') as f:
    PATTERNS = json.load(f)

def get_pattern(name):
    return next((p for p in PATTERNS if p['name'] == name), None)

def list_patterns():
    return PATTERNS
