"""
Tests unitaires pour la gestion des ACL (app.security.acl) — Dihya Coding.

Vérifie la gestion des rôles, la vérification des permissions et la robustesse des helpers ACL.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from backend.flask.app.securite import acl

class DummyUser:
    def __init__(self, roles=None, role=None):
        self.roles = roles if roles is not None else []
        self.role = role

def test_get_user_roles_with_roles():
    """Test récupération des rôles via l'attribut 'roles'."""
    user = DummyUser(roles=["admin", "user"])
    assert acl.get_user_roles(user) == ["admin", "user"]

def test_get_user_roles_with_role():
    """Test récupération du rôle unique via l'attribut 'role'."""
    user = DummyUser(role="guest")
    assert acl.get_user_roles(user) == ["guest"]

def test_get_user_roles_empty():
    """Test récupération des rôles pour un utilisateur sans rôle."""
    user = DummyUser()
    assert acl.get_user_roles(user) == []

def test_check_access_admin():
    """Test qu'un admin a accès à une permission admin."""
    user = DummyUser(roles=["admin"])
    assert acl.check_access(user, "access_admin_panel") is True

def test_check_access_user_denied():
    """Test qu'un user n'a pas accès à une permission admin."""
    user = DummyUser(roles=["user"])
    assert acl.check_access(user, "access_admin_panel") is False

def test_check_access_guest():
    """Test qu'un guest a accès à 'view_content' mais pas à 'edit_content'."""
    user = DummyUser(role="guest")
    assert acl.check_access(user, "view_content") is True
    assert acl.check_access(user, "edit_content") is False
