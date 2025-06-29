# Point d’entrée Python pour accéder aux GIFs de preview

from pathlib import Path

GIFS = {
    'preview1': Path(__file__).parent / 'preview1.gif',
    'preview2': Path(__file__).parent / 'preview2.gif',
}

def get_gif(name):
    """Retourne le chemin du GIF de preview demandé."""
    return GIFS.get(name, GIFS['preview1'])
