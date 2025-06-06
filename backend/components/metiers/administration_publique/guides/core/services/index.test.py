"""
Test d’import du point d’entrée JS services côté Python (présence du fichier)
"""
import os

def test_index_js_existe():
    assert os.path.exists('index.js')
