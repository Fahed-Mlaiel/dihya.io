# Point d’entrée Python pour les previews des assets de patterns

from pathlib import Path

PREVIEWS = {
    'svg': Path(__file__).parent / 'svg' / 'preview1.svg',
    'png': Path(__file__).parent / 'png' / 'preview1.png',
    'jpg': Path(__file__).parent / 'jpg' / 'preview1.jpg',
    'gif': Path(__file__).parent / 'gif' / 'preview1.gif',
    'webp': Path(__file__).parent / 'webp' / 'preview1.webp',
}

def get_preview(fmt):
    """Retourne le chemin du preview pour le format donné."""
    return PREVIEWS.get(fmt, PREVIEWS['svg'])
