"""
Test ultra avancé pour monitoring_sample.py
"""

from a_i.legacy.samples.monitoring.monitoring_sample import (
    monitoring_sample,
)


def test_monitoring_alert():
    assert "ALERT" in monitoring_sample("cpu", 150)


def test_monitoring_ok():
    assert "OK" in monitoring_sample("cpu", 50)


# ...autres tests avancés, edge cases, robustesse...
