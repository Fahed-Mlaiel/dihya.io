# test___init__.py
"""
Tests avancés pour sample_rgpd.py (validation RGPD).
"""
from mode.samples.validators.rgpd import sample_rgpd


class Dummy:
    has_consent = True


def test_validate_rgpd_true():
    d = Dummy()
    assert sample_rgpd.validate_rgpd(d) is True


def test_validate_rgpd_false():
    d = Dummy()
    d.has_consent = False
    assert sample_rgpd.validate_rgpd(d) is False


def test_validate_rgpd_missing():
    class NoConsent:
        pass

    assert sample_rgpd.validate_rgpd(NoConsent()) is False
