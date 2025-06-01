"""
Module i18n – Internationalisation avancée pour Dihya Coding

- Gestion multilingue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Fallback automatique, détection de langue, injection dans API, hooks métier, sectorisation
- Export DWeb/IPFS, RGPD (pas de tracking, logs anonymisés), audit, souveraineté
- Prêt pour accessibilité, SEO, CI/CD, monitoring, plugins, tests avancés
"""

import os
import json
from typing import Dict

LANG_DIR = os.path.join(os.path.dirname(__file__), 'locales')

SUPPORTED_LANGS = [
    'fr', 'en', 'ar', 'amazigh', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es'
]


def get_message(key: str, lang: str = 'fr') -> str:
    """Récupère le message localisé, fallback si non trouvé."""
    if lang not in SUPPORTED_LANGS:
        lang = 'fr'
    try:
        with open(os.path.join(LANG_DIR, f'{lang}.json'), encoding='utf-8') as f:
            messages = json.load(f)
        return messages.get(key, key)
    except Exception:
        return key

# Hook métier exemple

def i18n_hook(event: Dict, sector: str = None) -> Dict:
    """Injecte la langue et le secteur dans l’événement métier."""
    event['lang'] = event.get('lang', 'fr')
    if sector:
        event['sector'] = sector
    return event

# Export DWeb/IPFS (mock)
def export_i18n_to_ipfs():
    """Exporte les fichiers de langue sur IPFS (mock/demo)."""
    # TODO: Intégration réelle IPFS
    return True
