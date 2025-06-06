# index.test.py – Test d’import du point d’entrée global JS helpers (via Python)
import importlib

def test_import_index():
    try:
        importlib.import_module('templates.helpers.index')
    except Exception as e:
        assert False, f"L'import de index.js a échoué: {e}"
