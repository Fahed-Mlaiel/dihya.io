# validators.py - Exemple métier principal validators
def validate_data(data):
    return bool(data) and isinstance(data, dict) and len(data) > 0
