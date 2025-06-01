"""
Collecteur et endpoints de métriques de sécurité pour Dihya Coding.
"""
import threading
from typing import Dict
from flask import Blueprint, jsonify

_security_metrics = {
    "failed_logins": 0,
    "access_denied": 0,
    "alerts": [],
}
_metrics_lock = threading.Lock()

def increment_failed_login(user_id: str = None):
    with _metrics_lock:
        _security_metrics["failed_logins"] += 1
        if user_id:
            _security_metrics["alerts"].append(f"Failed login: {user_id}")

def increment_access_denied(user_id: str = None):
    with _metrics_lock:
        _security_metrics["access_denied"] += 1
        if user_id:
            _security_metrics["alerts"].append(f"Access denied: {user_id}")

def add_security_alert(alert: str):
    with _metrics_lock:
        _security_metrics["alerts"].append(alert)

def get_security_metrics() -> Dict:
    with _metrics_lock:
        return dict(_security_metrics)

security_metrics_blueprint = Blueprint("security_metrics", __name__)

@security_metrics_blueprint.route("/metrics/security", methods=["GET"])
def security_metrics_endpoint():
    return jsonify(get_security_metrics())
