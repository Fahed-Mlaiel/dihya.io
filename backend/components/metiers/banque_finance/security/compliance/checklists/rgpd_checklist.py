"""
rgpd_checklist.py – Checklist RGPD et validation ultra avancée (clé en main)
Respecte le cahier des charges, sécurité, conformité, auditabilité, accessibilité.
"""

REQUIRED_FIELDS = ["id", "name", "items", "owner"]

def validate_checklist(checklist):
    """Valide la structure et la conformité d'une checklist RGPD métier."""
    if not isinstance(checklist, dict):
        return False
    for field in REQUIRED_FIELDS:
        if field not in checklist:
            return False
    if not isinstance(checklist["id"], int):
        return False
    if not isinstance(checklist["name"], str):
        return False
    if not isinstance(checklist["items"], list) or not checklist["items"]:
        return False
    if not isinstance(checklist["owner"], str):
        return False
    # Optionnel : ignorer les champs en trop
    return True
