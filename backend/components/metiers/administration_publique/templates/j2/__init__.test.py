# __init__.test.py – Test d’import du point d’entrée Python j2 templates
import importlib

def test_import_j2_templates():
    mod = importlib.import_module('backend.components.metiers.threed.templates.j2')
    assert mod is not None
