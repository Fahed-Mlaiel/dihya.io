# __init__.test.py
"""Test d'import du point d'entrée Python core validators"""
import importlib

def test_import_core_validators_init():
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None
