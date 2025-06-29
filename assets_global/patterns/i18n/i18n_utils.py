# i18n_utils.py – Utilitaires Python pour i18n patterns

import os
import json

def load_i18n(lang_code):
    """Charge le fichier de traduction pour la langue/dialecte donnée."""
    path = os.path.join(os.path.dirname(__file__), f'i18n_{lang_code}.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}

def validate_i18n(lang_code):
    """Valide la structure du fichier i18n."""
    data = load_i18n(lang_code)
    return isinstance(data, dict)
