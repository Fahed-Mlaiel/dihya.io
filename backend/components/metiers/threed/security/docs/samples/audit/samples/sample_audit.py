# sample_audit.py
# Exemple d’intégration avancée pour l’audit

from helpers_audit import log_event, alert_on_suspicious_activity

log_event('LOGIN', {'user': 'Alice', 'status': 'success'})
alert = alert_on_suspicious_activity({'level': 'high', 'action': 'delete'})
print(alert)
