"""
test_usage_samples.py – Test ultra avancé pour usage_samples.py (guides.helpers.samples)

Ce fichier fournit un test d’exemple pour usage_samples.py.
"""
from usage_samples import get_usage_sample

def test_get_usage_sample():
    sample = get_usage_sample()
    assert sample["status"] == "ok"
    assert "data" in sample
