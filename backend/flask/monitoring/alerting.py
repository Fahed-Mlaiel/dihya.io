"""
Module d'alerting pour la surveillance du backend Dihya Coding.

Ce module permet d'envoyer des alertes (email, webhook, logs) en cas d'incident critique
(erreur applicative, dépassement de quota, indisponibilité d'un service, etc.).

Bonnes pratiques :
- Centraliser la logique d'alerting ici pour faciliter la maintenance.
- Ne jamais inclure de données sensibles dans les messages d'alerte.
- Prévoir plusieurs canaux d'alerte (mail, webhook, logs).
- Logger chaque alerte envoyée avec horodatage.
- Tester régulièrement le bon fonctionnement des alertes.

Exemple d'utilisation :
    from monitoring.alerting import send_alert
    send_alert("Erreur critique détectée", level="CRITICAL")

"""

import os
from datetime import datetime

ALERT_LOG_FILE = os.getenv("ALERT_LOG_FILE", "monitoring/alerts.log")

def send_alert(message, level="WARNING", channel="log"):
    """
    Envoie une alerte via le canal spécifié.
    :param message: Message d'alerte (str)
    :param level: Niveau de gravité ("INFO", "WARNING", "CRITICAL")
    :param channel: Canal d'alerte ("log", "email", "webhook")
    """
    timestamp = datetime.utcnow().isoformat()
    alert_entry = f"{timestamp} | {level.upper()} | {message}"

    if channel == "log":
        os.makedirs(os.path.dirname(ALERT_LOG_FILE), exist_ok=True)
        with open(ALERT_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(alert_entry + "\n")
    elif channel == "email":
        # TODO: Intégrer l'envoi d'email via un service sécurisé (ex: SendGrid)
        print(f"[ALERTE EMAIL] {alert_entry}")
    elif channel == "webhook":
        # TODO: Intégrer l'envoi d'une alerte via webhook externe
        print(f"[ALERTE WEBHOOK] {alert_entry}")
    else:
        print(f"[ALERTE INCONNUE] {alert_entry}")

def alerting_hook(event, sector=None):
    """Injecte la logique métier et le secteur dans l’événement d’alerte."""
    event['sector'] = sector or 'default'
    return event

# Export DWeb/IPFS (mock)
def export_alerts_to_ipfs():
    """Exporte les alertes sur IPFS (mock/demo)."""
    # TODO: Intégration réelle IPFS
    return True
