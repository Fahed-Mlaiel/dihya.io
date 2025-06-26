# Exemple avancé de validation d’input (Python)
def validate_input(input):
    return isinstance(input, str) and len(input) > 0
