# test_alerts.py – Tests d’envoi d’alertes sécurité (pytest)
from backend.firewall.alerts.send_alert import send_security_alert

def test_send_alert(monkeypatch):
    sent = {}
    def fake_send_message(msg):
        sent['ok'] = True
    monkeypatch.setattr('smtplib.SMTP.send_message', fake_send_message)
    send_security_alert('Test', 'Alerte test', 'admin@dihya.app')
    assert sent.get('ok')
