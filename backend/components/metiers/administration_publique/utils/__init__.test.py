"""
__init__.test.py – Tests unitaires Python pour __init__.py (import dynamique)
"""
import importlib
import os
import glob

def test_import_all_utils():
    utils_dir = os.path.dirname(__file__)
    py_files = [f for f in glob.glob(os.path.join(utils_dir, '*.py')) if not f.endswith('__init__.py')]
    for file in py_files:
        module_name = os.path.splitext(os.path.basename(file))[0]
        try:
            importlib.import_module(f'.{module_name}', 'backend.components.metiers.threed.utils')
        except Exception as e:
            assert False, f"Erreur d'import: {module_name} ({e})"
