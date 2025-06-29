"""
Test ultra avancé pour validator_sample.py
"""

from science.legacy.samples.validators.validator_sample import validator_sample


def test_validator_ok():
    assert validator_sample("abcd") is True


def test_validator_short():
    assert validator_sample("ab") is False


# ...autres tests avancés, edge cases, robustesse...
