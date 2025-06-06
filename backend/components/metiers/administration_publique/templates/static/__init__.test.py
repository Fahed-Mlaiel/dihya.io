# __init__.test.py – Test d’import du point d’entrée Python static templates
import importlib

def test_import_static_templates():
    mod = importlib.import_module('backend.components.metiers.threed.templates.static')
    assert mod is not None
