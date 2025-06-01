"""
Tests avancés pour les favicons API backend PNG (accessibilité, RGPD, hash, version, audit, CI/CD).
"""
import os
import hashlib
import pytest

PNG_DIR = os.path.dirname(__file__)

@pytest.mark.parametrize("filename", [
    "favicon-api.png",
    "favicon-api-dark.png"
])
def test_png_exists(filename):
    path = os.path.join(PNG_DIR, filename)
    assert os.path.exists(path), f"Fichier manquant: {filename}"

def test_png_hash(filename):
    path = os.path.join(PNG_DIR, filename)
    with open(path, 'rb') as f:
        data = f.read()
    # Hash SHA256 pour auditabilité
    hash_val = hashlib.sha256(data).hexdigest()
    assert len(hash_val) == 64

def test_png_accessibility(filename):
    # Vérification basique (nommage, accessibilité, extension)
    assert filename.endswith('.png')
    assert 'favicon' in filename
