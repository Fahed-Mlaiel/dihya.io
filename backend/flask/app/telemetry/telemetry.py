"""
Module de télémétrie centralisée – Dihya Coding

Ce module fournit des fonctions pour la collecte, l’agrégation et l’export des logs, traces et métriques
de la plateforme Dihya Coding, dans une optique d’observabilité, d’auditabilité et de sécurité.

Bonnes pratiques :
- Centraliser la configuration des logs et métriques ici
- Ne jamais logger de données sensibles
- Prévoir l’export compatible Prometheus/OpenTelemetry
- Documenter chaque fonction et format de métrique
"""

import logging
import time
from typing import Dict, Any

_METRICS = {}

def configure_logging(level=logging.INFO):
    """
    Configure le logging global de l’application.

    Args:
        level (int): Niveau de log (INFO, WARNING, ERROR…)
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s"
    )

def log_event(event_name: str, payload: Dict[str, Any]):
    """
    Logge un événement métier ou technique.

    Args:
        event_name (str): Nom de l’événement.
        payload (dict): Données associées (jamais de données sensibles).
    """
    logger = logging.getLogger("dihya.telemetry")
    logger.info(f"Event: {event_name} | Payload: {payload}")

def record_metric(name: str, value: float = 1.0, labels: Dict[str, str] = None):
    """
    Enregistre une métrique personnalisée (compteur, gauge…).

    Args:
        name (str): Nom de la métrique.
        value (float): Valeur à incrémenter ou fixer.
        labels (dict, optional): Labels additionnels (ex: {"endpoint": "/api/v1/login"}).
    """
    key = name
    if labels:
        key += "|" + "|".join(f"{k}:{v}" for k, v in sorted(labels.items()))
    _METRICS[key] = _METRICS.get(key, 0) + value

def export_metrics_prometheus() -> str:
    """
    Exporte les métriques au format Prometheus.

    Returns:
        str: Représentation texte des métriques.
    """
    lines = []
    for key, value in _METRICS.items():
        metric, *label_parts = key.split("|")
        if label_parts:
            labels = ",".join(label_parts)
            lines.append(f'{metric}{{{labels}}} {value}')
        else:
            lines.append(f"{metric} {value}")
    return "\n".join(lines)

def timeit(metric_name: str):
    """
    Décorateur pour mesurer la durée d’exécution d’une fonction et l’enregistrer comme métrique.

    Args:
        metric_name (str): Nom de la métrique de durée.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            record_metric(metric_name, duration)
            return result
        return wrapper
    return decorator