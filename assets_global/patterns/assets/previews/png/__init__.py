# Point d’entrée Python pour accéder aux PNGs de preview

from pathlib import Path

PNGS = {
    'preview1': Path(__file__).parent / 'preview1.png',
    'preview2': Path(__file__).parent / 'preview2.png',
}

def get_png(name):
    """Retourne le chemin du PNG de preview demandé."""
    return PNGS.get(name, PNGS['preview1'])
