# Validateurs Python automobile ultra avancés
def validate_automobile(data):
    required = ['nom', 'statut']
    for field in required:
        if field not in data or not data[field]:
            return False
    return True
