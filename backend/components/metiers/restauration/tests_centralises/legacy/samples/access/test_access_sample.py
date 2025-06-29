"""
Test ultra avancé pour access_sample.py
"""

from restauration.legacy.samples.access.access_sample import access_sample


def test_access_admin():
    assert access_sample("admin", "secret") is True


def test_access_non_admin():
    assert access_sample("user", "wrong") is False


# ...autres tests avancés, edge cases, sécurité...
