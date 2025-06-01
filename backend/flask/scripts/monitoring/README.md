# monitoring/ — Scripts de monitoring et supervision (Dihya Coding)

Ce dossier regroupe les scripts de monitoring et de supervision pour le backend Flask Dihya Coding.

## Objectif

- Surveiller la santé, la disponibilité et la performance des services backend.
- Détecter proactivement les incidents, anomalies ou dégradations de service.
- Faciliter l’intégration avec des outils de supervision (Prometheus, Grafana, Zabbix, etc.).

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger les résultats de monitoring pour audit et analyse.
- Prévoir des alertes en cas d’anomalie détectée (email, Slack, webhook, etc.).
- Ne jamais exposer de secrets ou de données sensibles dans les logs ou les alertes.
- Tester régulièrement les scripts pour garantir leur fiabilité.

## Exemple de structure

- `check_health.sh` : vérification de l’état de santé des services.
- `monitor_performance.py` : suivi des temps de réponse et de la charge.
- `alert_on_failure.sh` : envoi d’alertes en cas d’incident détecté.

## Exemple d’utilisation

```bash
bash check_health.sh
python monitor_performance.py --interval 60