"""
Test centralisé security threed (Python).
"""

import pytest
from ...security import check_access, audit_log, validate_token


def test_access_denied_without_token():
    with pytest.raises(Exception):
        check_access(None)


def test_valid_jwt_token():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    assert validate_token(token) is True


def test_audit_log():
    result = audit_log({"action": "login", "user": "admin"})
    assert "timestamp" in result
