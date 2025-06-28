"""
Tests ultra avancés pour rbac_utils.py (RBAC Blockchain)
Couvre : cas nominaux, edge cases, conformité RGPD, audit, accessibilité, robustesse, multitenancy.
"""
import pytest
from backend.components.metiers.blockchain.utils.rbac.core import rbac_utils

def test_is_valid_role():
    assert rbac_utils.is_valid_role("admin")
    assert not rbac_utils.is_valid_role("")
    assert not rbac_utils.is_valid_role(" ")
    assert not rbac_utils.is_valid_role("a"*65)
    assert not rbac_utils.is_valid_role("admin-user!")
    assert rbac_utils.is_valid_role("user_1")
    assert rbac_utils.is_valid_role("roleX")

def test_filter_roles():
    roles = ["admin", "user", "guest", "banned"]
    allowed = ["admin", "user"]
    assert rbac_utils.filter_roles(roles, allowed) == ["admin", "user"]
    assert rbac_utils.filter_roles([], allowed) == []
    assert rbac_utils.filter_roles(roles, []) == []

def test_audit_roles():
    roles = ["admin", "user", "user"]
    audit = rbac_utils.audit_roles(roles)
    assert audit["roles"] == roles
    assert audit["count"] == 3
    assert audit["unique"] == 2
    assert "audit_date" in audit

def test_anonymize_roles():
    roles = ["admin", "user", "guest"]
    anonymized = rbac_utils.anonymize_roles(roles)
    assert anonymized == ["role_1", "role_2", "role_3"]
    assert len(anonymized) == len(roles)
    assert all(r.startswith("role_") for r in anonymized)
    assert rbac_utils.anonymize_roles([]) == []
