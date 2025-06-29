# Point d’entrée Python pour la documentation des assets de patterns

from pathlib import Path

DOCS = {
    'fr': Path(__file__).parent / 'assets_doc_fr.md',
    'en': Path(__file__).parent / 'assets_doc_en.md',
    'ar': Path(__file__).parent / 'assets_doc_ar.md',
    'ber': Path(__file__).parent / 'assets_doc_ber.md',
}

def get_doc(lang):
    """Retourne le chemin du fichier de documentation pour la langue donnée."""
    return DOCS.get(lang, DOCS['fr'])
