# Point d’entrée Python pour accéder aux WEBPs de preview

from pathlib import Path

WEBPS = {
    'preview1': Path(__file__).parent / 'preview1.webp',
    'preview2': Path(__file__).parent / 'preview2.webp',
}

def get_webp(name):
    """Retourne le chemin du WEBP de preview demandé."""
    return WEBPS.get(name, WEBPS['preview1'])
