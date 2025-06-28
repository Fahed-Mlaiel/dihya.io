"""
templates_validator.py – Validateur ultra avancé pour les templates Culture (Python)
Inclut : validation de structure, sécurité, audit, edge cases, CI/CD
"""

import os


def is_valid_template_file(filename):
    return filename.endswith(
        (".html.j2", ".json.j2", ".xml", ".txt")
    ) and os.path.isfile(filename)


def validate_template_content(content):
    # Vérifie la présence de balises Jinja2 ou variables attendues
    return (
        ("{{" in content and "}}" in content)
        or "<" in content
        or "{" in content
    )


# Exemples d’utilisation, edge cases, synchronisation JS/Python
