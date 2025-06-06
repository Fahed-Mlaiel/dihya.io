"""
Test unitaire pour sample_service.py
"""
from .sample_service import run
def test_run():
    assert run() == 'Service exécuté!'
