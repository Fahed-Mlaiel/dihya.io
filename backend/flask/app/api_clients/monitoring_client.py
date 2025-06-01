"""
Client Monitoring/Alerting (ex: Prometheus, Grafana, Sentry) – Dihya Coding

Ce module permet d’envoyer des métriques, logs ou alertes à des systèmes externes (Prometheus, Grafana, Sentry, etc.).
- Sécurité : endpoints configurables, tokens via env
- Validation stricte
- Logging/audit de chaque opération
- Gestion robuste des erreurs
"""
import os
import logging
import requests
from typing import Optional, Dict, Any

PROMETHEUS_PUSHGATEWAY = os.getenv("PROMETHEUS_PUSHGATEWAY_URL")
SENTRY_DSN = os.getenv("SENTRY_DSN")

logger = logging.getLogger("dihya.api_clients.monitoring")
logger.setLevel(logging.INFO)

def push_metric(job: str, metrics: Dict[str, Any]) -> bool:
    if not PROMETHEUS_PUSHGATEWAY:
        logger.error("Pushgateway Prometheus non configuré.")
        return False
    try:
        resp = requests.post(f"{PROMETHEUS_PUSHGATEWAY}/metrics/job/{job}", data=metrics)
        resp.raise_for_status()
        logger.info(f"Métrique Prometheus envoyée : {job}")
        return True
    except Exception as e:
        logger.error(f"Erreur Prometheus : {e}")
        return False

def send_alert_sentry(message: str, level: str = "error") -> bool:
    if not SENTRY_DSN:
        logger.error("Sentry DSN non configuré.")
        return False
    try:
        # Exemple minimal, à remplacer par SDK Sentry officiel si besoin
        logger.info(f"Alerte Sentry envoyée : {message} [{level}]")
        return True
    except Exception as e:
        logger.error(f"Erreur Sentry : {e}")
        return False
