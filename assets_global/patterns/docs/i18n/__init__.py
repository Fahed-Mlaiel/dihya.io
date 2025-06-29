# __init__.py – i18n Patterns Docs

"""
Point d’entrée Python pour l’internationalisation de la documentation des patterns.
Permet d’importer dynamiquement les fichiers de traduction selon la langue.
"""

import os
import json

def load_i18n(lang_code):
    """Charge le fichier de traduction pour la langue/dialecte donnée."""
    path = os.path.join(os.path.dirname(__file__), f'i18n_{lang_code}.json')
    with open(path, encoding='utf-8') as f:
        return json.load(f)
