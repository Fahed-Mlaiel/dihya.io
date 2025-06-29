# test_policies.py
"""
Tests ultra avancés pour la conformité des politiques de sécurité (clé en main).
"""
import pytest
from backend.components.metiers.seo.security.core.policy.policy import validate_policy, REQUIRED_POLICY_FIELDS


def test_valid_policy():
    policy = {
        "id": 1,
        "title": "Chiffrement des données",
        "rules": ["at-rest", "in-transit"],
        "owner": "ciso"
    }
    assert validate_policy(policy) is True


def test_missing_required_fields():
    policy = {"id": 2, "rules": ["at-rest"]}
    assert validate_policy(policy) is False


def test_empty_rules():
    policy = {"id": 3, "title": "Vide", "rules": [], "owner": "ciso"}
    assert validate_policy(policy) is False


def test_invalid_types():
    policy = {"id": "x", "title": 123, "rules": "at-rest", "owner": None}
    assert validate_policy(policy) is False


def test_required_fields_constant():
    assert set(REQUIRED_POLICY_FIELDS) == {"id", "title", "rules", "owner"}


def test_extra_fields_are_ignored():
    policy = {"id": 4, "title": "Extra", "rules": ["at-rest"], "owner": "ciso", "foo": "bar"}
    assert validate_policy(policy) is True
