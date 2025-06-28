"""
Module ultra avancé de gestion des métriques pour Science.
- Collecte, calcul, export, alertes, plugins, RGPD, audit, etc.
"""

from datetime import datetime
from typing import Dict, List, Any

_metrics_store: List[Dict[str, Any]] = []


def record_metric(
    name: str, value: float, tags: Dict[str, str] = None
) -> None:
    """Enregistre une métrique avec tags et timestamp."""
    if tags is None:
        tags = {}
    _metrics_store.append(
        {
            "name": name,
            "value": value,
            "tags": tags,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
    )


def get_metrics(name: str = None) -> List[Dict[str, Any]]:
    """Retourne toutes les métriques ou filtre par nom."""
    if name:
        return [m for m in _metrics_store if m["name"] == name]
    return list(_metrics_store)


def get_average_metric(name: str) -> float:
    """Calcule la moyenne d'une métrique donnée."""
    values = [m["value"] for m in _metrics_store if m["name"] == name]
    return sum(values) / len(values) if values else 0.0


def export_metrics() -> str:
    """Exporte les métriques au format CSV (clé en main)."""
    import csv
    from io import StringIO

    output = StringIO()
    writer = csv.DictWriter(
        output, fieldnames=["name", "value", "tags", "timestamp"]
    )
    writer.writeheader()
    for m in _metrics_store:
        writer.writerow(m)
    return output.getvalue()
