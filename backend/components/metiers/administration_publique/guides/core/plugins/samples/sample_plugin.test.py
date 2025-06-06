"""
Test unitaire pour sample_plugin.py
"""
from .sample_plugin import run
def test_run():
    assert run() == 'Plugin exécuté!'
