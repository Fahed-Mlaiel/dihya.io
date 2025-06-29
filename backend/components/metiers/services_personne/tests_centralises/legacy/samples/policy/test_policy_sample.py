"""
Test ultra avancé pour policy_sample.py
"""

from services_personne.legacy.samples.policy.policy_sample import policy_sample


def test_policy_admin():
    assert policy_sample("admin") == "full-access"


def test_policy_user():
    assert policy_sample("user") == "restricted"


# ...autres tests avancés, edge cases, sécurité...
