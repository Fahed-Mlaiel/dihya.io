# test_checklists.py
"""
Tests ultra avancés pour la conformité des checklists de sécurité (clé en main).
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from backend.components.metiers.construction.security.compliance.checklists.rgpd_checklist import validate_checklist, REQUIRED_FIELDS


def test_valid_checklist():
    checklist = {
        "id": 1,
        "name": "Sécurité API",
        "items": ["auth", "logging", "rate-limit"],
        "owner": "admin"
    }
    assert validate_checklist(checklist) is True


def test_missing_required_fields():
    checklist = {"id": 2, "items": ["auth"]}
    assert validate_checklist(checklist) is False


def test_empty_items():
    checklist = {"id": 3, "name": "Vide", "items": [], "owner": "admin"}
    assert validate_checklist(checklist) is False


def test_invalid_types():
    checklist = {"id": "x", "name": 123, "items": "auth", "owner": None}
    assert validate_checklist(checklist) is False


def test_required_fields_constant():
    assert set(REQUIRED_FIELDS) == {"id", "name", "items", "owner"}


def test_extra_fields_are_ignored():
    checklist = {"id": 4, "name": "Extra", "items": ["auth"], "owner": "admin", "foo": "bar"}
    assert validate_checklist(checklist) is True
