"""
Test ultra avancé pour compliance_sample.py
"""

from voyage.legacy.samples.compliance.compliance_sample import (
    compliance_sample,
)


def test_compliance_consent():
    assert compliance_sample({"consent": True}) is True


def test_compliance_no_consent():
    assert compliance_sample({}) is False


# ...autres tests avancés, edge cases, conformité...
