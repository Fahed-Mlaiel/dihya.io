# Point d’entrée Python pour l’i18n des assets de patterns

import json
from pathlib import Path

I18N_FILES = {
    'fr': Path(__file__).parent / 'i18n_fr.json',
    'en': Path(__file__).parent / 'i18n_en.json',
    'ar': Path(__file__).parent / 'i18n_ar.json',
    'ber': Path(__file__).parent / 'i18n_ber.json',
    # ...ajouter les autres langues ici
}

def get_i18n(lang):
    """Retourne le contenu i18n pour la langue donnée."""
    path = I18N_FILES.get(lang, I18N_FILES['fr'])
    with open(path, encoding='utf-8') as f:
        return json.load(f)
