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

def valider_email(email):
    return isinstance(email, str) and '@' in email and '.' in email

def valider_note(note):
    return isinstance(note, (int, float)) and 0 <= note <= 20

def valider_role(role):
    return role in ['admin', 'enseignant', 'étudiant', 'invité']

def valider_rgpd(data):
    return 'consentement' in data and data['consentement'] is True
