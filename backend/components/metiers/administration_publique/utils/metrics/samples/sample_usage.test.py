# sample_usage.test.py
"""Tests unitaires avancés pour les exemples metrics Python"""
from ..core import metrics
import json
import pytest

def test_calculer_moyenne():
    with open('sample_metrics_data.json') as f:
        data = json.load(f)["metrics"]
    assert abs(metrics.calculer_moyenne(data) - 15.814) < 0.01

def test_calculer_mediane():
    with open('sample_metrics_data.json') as f:
        data = json.load(f)["metrics"]
    assert metrics.calculer_mediane(data) == 3.5

def test_moyenne_vide():
    with pytest.raises(Exception):
        metrics.calculer_moyenne([])
