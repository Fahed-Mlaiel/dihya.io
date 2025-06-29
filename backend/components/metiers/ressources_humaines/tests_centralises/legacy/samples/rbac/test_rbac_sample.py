"""
Test ultra avancé pour rbac_sample.py
"""

from ressources_humaines.legacy.samples.rbac.rbac_sample import rbac_sample


def test_rbac_admin():
    assert "tous les droits" in rbac_sample("alice", "admin")


def test_rbac_user():
    assert "accès restreint" in rbac_sample("bob", "user")


def test_rbac_empty_user():
    assert "tous les droits" in rbac_sample("", "admin")
    assert "accès restreint" in rbac_sample("", "user")


def test_rbac_none_user():
    assert "tous les droits" in rbac_sample(None, "admin")
    assert "accès restreint" in rbac_sample(None, "user")


def test_rbac_unknown_role():
    assert "accès restreint" in rbac_sample("eve", "guest")


# ...autres tests avancés, edge cases, sécurité...
