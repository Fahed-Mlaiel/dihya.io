"""
Point d’entrée Python pour l’i18n patterns
Permet d’importer dynamiquement les fichiers de traduction selon la langue/dialecte
"""
import os
import json

def load_i18n(lang_code):
    path = os.path.join(os.path.dirname(__file__), f'i18n_{lang_code}.json')
    with open(path, encoding='utf-8') as f:
        return json.load(f)
