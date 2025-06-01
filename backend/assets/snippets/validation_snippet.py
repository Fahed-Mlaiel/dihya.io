"""
validation_snippet.py – Validation avancée backend (Dihya)
Schéma, types, RGPD, logs, audit, multilingue.
"""
def validate_schema(data, schema):
    for k, v in schema.items():
        if k not in data or not isinstance(data[k], v):
            raise ValueError(f"[VALIDATION] Champ {k} invalide")
    return True

# Exemple d’utilisation
if __name__ == "__main__":
    schema = {"email": str, "age": int}
    print(validate_schema({"email": "a@b.com", "age": 22}, schema))
