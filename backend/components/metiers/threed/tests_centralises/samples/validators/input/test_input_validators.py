# test___init__.py
"""
Tests avancés pour sample_input.py (validation d'input).
"""
from threed.samples.validators.input import sample_input


def test_validate_input_valid():
    assert sample_input.validate_input("valide") is True


def test_validate_input_empty():
    assert sample_input.validate_input("") is False


def test_validate_input_non_string():
    assert sample_input.validate_input(123) is False
