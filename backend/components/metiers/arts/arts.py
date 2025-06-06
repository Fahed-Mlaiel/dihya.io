# Module principal Arts

def get_expositions():
    return [
        {"id": 1, "nom": "Exposition Impressionniste", "lieu": "Musée d'Orsay", "date": "2025-06-01"},
        {"id": 2, "nom": "Atelier Sculpture Moderne", "lieu": "Ateliers Beaux-Arts", "date": "2025-07-15"}
    ]

def get_oeuvres():
    return [
        {"id": 1, "nom": "Impression, soleil levant", "artiste": "Claude Monet", "type": "peinture"},
        {"id": 2, "nom": "La Classe de danse", "artiste": "Edgar Degas", "type": "peinture"}
    ]

def get_artistes():
    return [
        {"id": 1, "nom": "Claude Monet"},
        {"id": 2, "nom": "Edgar Degas"}
    ]

def rechercher_oeuvre(nom):
    return [o for o in get_oeuvres() if nom.lower() in o["nom"].lower()]
