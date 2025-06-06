# __init__.test.py
"""Test d'import du point d'entrée Python samples validators"""
import importlib

def test_import_samples_validators_init():
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None
