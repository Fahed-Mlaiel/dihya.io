# alerts/

Alerting avancé pour le monitoring de sécurité (Prometheus, scripts, etc.).

- `alerts.js`, `alerts.py` : scripts principaux
- `custom_alert_script.sh`, `prometheus_alerts.yml` : exemples d’alertes
- `__init__.js`, `__init__.py` : points d’entrée
- `.keep` : versionnement du dossier

## Bonnes pratiques
- Centraliser toute logique d’alerting ici.
- Ajouter des exemples dans `samples/alerts/`.
