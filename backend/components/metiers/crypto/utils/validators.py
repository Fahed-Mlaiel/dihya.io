"""
Validateurs avancés pour Environnement.
Permet de garantir la conformité des entités métier.
"""

def validate_environnement(data):
    """
    Valide les données d'une entité environnementale.
    Lève une exception si le nom est manquant ou si le statut est invalide.
    """
    if not data.get("nom"):
        raise ValueError("Nom requis")
    if data.get("statut") not in (None, "actif", "inactif", "archivé"):
        raise ValueError("Statut invalide")
    return True

def is_valid_address(address):
    """
    Valide une adresse crypto (exemple simplifié).
    """
    return isinstance(address, str) and address.startswith('0x') and len(address) == 42

def is_strong_password(password):
    """
    Vérifie la robustesse d'un mot de passe (exemple simplifié).
    """
    return isinstance(password, str) and len(password) >= 12 and any(c.isdigit() for c in password)
