# Point d’entrée Python pour accéder aux JPGs de preview

from pathlib import Path

JPGS = {
    'preview1': Path(__file__).parent / 'preview1.jpg',
    'preview2': Path(__file__).parent / 'preview2.jpg',
}

def get_jpg(name):
    """Retourne le chemin du JPG de preview demandé."""
    return JPGS.get(name, JPGS['preview1'])
