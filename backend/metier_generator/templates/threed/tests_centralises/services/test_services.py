"""
Tests centralisés pour les services threed (Python)
"""

from ...services import run_service, get_service_status


def test_run_notification_service():
    result = run_service("notification", {"message": "test"})
    assert result["success"] is True


def test_monitoring_service_status():
    status = get_service_status("monitoring")
    assert status in ["running", "stopped"]
