# __init__.test.py – Test d'import du point d'entrée Python du sous-module router
import importlib

def test_import_router():
    module = importlib.import_module('backend.components.metiers.threed.views.router')
    assert hasattr(module, 'router')
