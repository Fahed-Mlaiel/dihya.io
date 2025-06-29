# Point d’entrée Python pour accéder à la documentation patterns

from pathlib import Path

docs = {
    'reference': Path(__file__).parent / 'patterns_reference.md',
    'integration': Path(__file__).parent / 'integration_guide.md',
    'architecture': Path(__file__).parent / 'architecture.md',
    'user_fr': Path(__file__).parent / 'user_guide_fr.md',
    'user_en': Path(__file__).parent / 'user_guide_en.md',
    'user_ar': Path(__file__).parent / 'user_guide_ar.md',
    'user_ber': Path(__file__).parent / 'user_guide_ber.md',
}

def get_doc(name):
    """Retourne le chemin du fichier de documentation demandé."""
    return docs.get(name, docs['reference'])
