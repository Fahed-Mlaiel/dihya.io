"""
Fonctions de rendu pour Environnement.
Permet de générer des vues textuelles ou HTML pour les entités métier.
"""

def render_view(data):
    """
    Génère une vue textuelle pour une entité environnementale.
    Peut être étendue pour générer du HTML ou du JSON.
    """
    return f"Vue environnementale: {data}"
