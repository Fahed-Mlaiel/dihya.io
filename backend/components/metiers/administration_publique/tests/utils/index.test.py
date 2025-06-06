# index.test.py – Test d'import global du point d'entrée utils (Python)
import importlib

def test_import_utils_index():
    mod = importlib.import_module('tests.utils.index')
    assert mod is not None
