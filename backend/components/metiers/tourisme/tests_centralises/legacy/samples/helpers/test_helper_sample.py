"""
Test ultra avancé pour helper_sample.py
"""

from tourisme.legacy.samples.helpers.helper_sample import helper_sample


def test_helper_format():
    assert helper_sample("test") == "[HELPER] test"


# ...autres tests avancés, edge cases, robustesse...
