# sample_usage.test.py
"""Tests unitaires avancés pour les exemples validators Python"""
from ..core import validators
import json
import pytest

def test_validate_email():
    with open('sample_validators_data.json') as f:
        data = json.load(f)
    assert validators.validate_email(data['email'])

def test_validate_required():
    with open('sample_validators_data.json') as f:
        data = json.load(f)
    assert validators.validate_required(data['requiredField'])
    assert not validators.validate_required('')
