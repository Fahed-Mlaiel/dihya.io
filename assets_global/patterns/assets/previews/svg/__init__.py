# Point d’entrée Python pour accéder aux SVGs de preview

from pathlib import Path

SVGS = {
    'preview1': Path(__file__).parent / 'preview1.svg',
    'preview2': Path(__file__).parent / 'preview2.svg',
}

def get_svg(name):
    """Retourne le chemin du SVG de preview demandé."""
    return SVGS.get(name, SVGS['preview1'])
