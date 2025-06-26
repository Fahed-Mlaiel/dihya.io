# input_validator.py – Validation des entrées


def validate_input(data):
    # Exemple de validation avancée
    if not isinstance(data, dict):
        raise ValueError("Entrée invalide : doit être un dictionnaire")
    if "user" not in data or "action" not in data:
        raise ValueError("Entrée invalide : champs requis manquants")
    return True
