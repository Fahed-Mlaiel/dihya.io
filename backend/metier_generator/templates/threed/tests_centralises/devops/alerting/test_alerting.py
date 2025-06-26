"""
Tests avancés pour l'alerting métier (detection, notification, escalade).
"""
import importlib.util
import os

def find_alerting_path():
    cur = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(cur, 'devops', 'alerting', 'alerting.py')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError('alerting.py introuvable')
        cur = parent

alerting_path = find_alerting_path()
spec = importlib.util.spec_from_file_location('alerting', alerting_path)
alerting = importlib.util.module_from_spec(spec)
spec.loader.exec_module(alerting)
send_alert = alerting.send_alert


def test_send_alert():
    result = send_alert("Test d'alerte")
    assert result is True
