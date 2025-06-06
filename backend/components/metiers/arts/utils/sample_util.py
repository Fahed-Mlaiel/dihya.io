# Exemple d'utilitaire pour Arts

def util_arts():
    """Retourne un message de succès pour l'utilitaire Arts."""
    return 'Utilitaire Arts OK'

def format_artwork(artwork):
    """Formate une œuvre d'art en chaîne lisible."""
    return f"{artwork['nom']} ({artwork['type']})"

def validate_artwork(artwork):
    """Valide la structure d'une œuvre d'art."""
    return all(k in artwork for k in ("id", "nom", "type"))
