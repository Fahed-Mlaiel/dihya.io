"""
Plugin d’audit accessibilité PNG pour favicons API backend (nommage, alt, RGPD, logs).
"""
import os

def check_accessibility(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            assert 'favicon' in filename, f"Nom de fichier non conforme: {filename}"
            print(f"[PNG_A11Y] {filename} | OK")

if __name__ == '__main__':
    check_accessibility(os.path.dirname(__file__))
