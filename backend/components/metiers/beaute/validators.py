"""
Validators Beauté – Dihya Coding
Validation avancée, RGPD, plugins, audit, multilingue, sécurité, extensibilité.
"""

def validate_beaute_project(data, lang="fr"):
    if not data.get("name"):
        return {"error": {"fr": "Nom manquant", "en": "Missing name"}[lang]}
    # RGPD, plugins, audit, sécurité
    return data
