# Script de génération d'images placeholder pour tous les formats previews

"""
Ce script Python crée automatiquement des fichiers d'exemple (1x1 pixel transparent ou blanc)
pour chaque format d'assets de preview (png, jpg, gif, webp) dans la structure attendue.
"""

from PIL import Image
import os

# Dossiers cibles et formats
base = 'assets_global/patterns/assets/previews'
formats = [
    ('png', 'png', 'RGBA'),
    ('jpg', 'jpg', 'RGB'),
    ('gif', 'gif', 'RGBA'),
    ('webp', 'webp', 'RGBA'),
]

for fmt_folder, ext, mode in formats:
    folder = os.path.join(base, fmt_folder)
    for name in ['preview1', 'preview2']:
        path = os.path.join(folder, f'{name}.{ext}')
        if not os.path.exists(path):
            if mode == 'RGB':
                img = Image.new('RGB', (1, 1), (255, 255, 255))
            else:
                img = Image.new('RGBA', (1, 1), (255, 255, 255, 0))
            img.save(path)

print('Images placeholder générées pour tous les formats.')
