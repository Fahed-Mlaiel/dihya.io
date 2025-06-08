# helpers_audit.py
# Helpers avancés pour la traçabilité, logs, forensic, alerting

def log_event(event_type, details):
    """Simule la journalisation d'un événement"""
    print(f"[AUDIT] {event_type}: {details}")

def alert_on_suspicious_activity(activity):
    """Simule une alerte sur activité suspecte"""
    if activity.get('level') == 'high':
        return 'ALERT: Suspicious activity detected!'
    return 'Activity normal.'
