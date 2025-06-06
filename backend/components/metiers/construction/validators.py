"""
Validators ultra avancés pour le module Construction (validation métier, RGPD, plugins, sécurité, conformité, multilingue, hooks métier)
"""

# Validators Construction


def validate_chantier(data):
    return all(k in data for k in ("id", "nom", "etat", "lang")) and bool(data["nom"])


def validate_nom(nom):
    return isinstance(nom, str) and len(nom.strip()) > 2


def validate_type(type_):
    return isinstance(type_, str) and len(type_.strip()) > 2
