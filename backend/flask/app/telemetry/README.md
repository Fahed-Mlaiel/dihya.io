# telemetry

Documentation interne Dihya Coding.

## Objectif

Ce dossier centralise tous les outils, modules et scripts liés à l’observabilité : logs, traces, métriques, événements métier et sécurité pour la plateforme Dihya Coding.

## Bonnes pratiques

- Centraliser la configuration des logs, traces et métriques pour tout le backend.
- Utiliser un bus d’événements pour la traçabilité transverse (voir `event_bus.py`).
- Logger chaque opération critique (auth, paiement, génération, etc.) avec horodatage.
- Ne jamais inclure de données sensibles dans les logs ou événements.
- Prévoir l’export et l’agrégation des métriques pour le monitoring (Prometheus, OpenTelemetry…).
- Documenter chaque module et chaque format d’événement.

## Structure recommandée

```
telemetry/
├── README.md
├── event_bus.py         # Bus d’événements interne (audit, monitoring…)
├── metrics.py           # Collecte et export des métriques (à ajouter)
├── logs_config.py       # Configuration centralisée des logs (à ajouter)
└── ...                 # Autres modules d’observabilité
```

## Exemple d’utilisation

```python
from telemetry.event_bus import EventBus

bus = EventBus()
bus.publish("user_login", {"user_id": 42, "ip": "1.2.3.4"})
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*