"""
Test ultra avancé pour rgpd_sample.py
"""

from seo.legacy.samples.rgpd.rgpd_sample import rgpd_sample


def test_rgpd_export():
    result = rgpd_sample("alice")
    assert result["user"] == "alice"
    assert result["export"] is True
    assert isinstance(result["date"], str)


def test_rgpd_export_empty_user():
    result = rgpd_sample("")
    assert result["user"] == ""
    assert result["export"] is True
    assert isinstance(result["date"], str)


def test_rgpd_export_none_user():
    result = rgpd_sample(None)
    assert result["user"] is None
    assert result["export"] is True
    assert isinstance(result["date"], str)


def test_rgpd_export_audit_date_format():
    import re

    result = rgpd_sample("bob")
    # Vérifie format ISO 8601
    assert re.match(r"\d{4}-\d{2}-\d{2}T", result["date"])

# ...autres tests avancés, edge cases, conformité RGPD...
