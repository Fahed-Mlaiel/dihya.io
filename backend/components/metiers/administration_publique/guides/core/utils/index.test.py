"""
Test d’import du point d’entrée JS utils côté Python (présence du fichier)
"""
import os

def test_index_js_existe():
    assert os.path.exists('index.js')
