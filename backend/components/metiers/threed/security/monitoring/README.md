# monitoring/

Ce dossier regroupe les modules de monitoring de sécurité :
- `alerts/` : alerting Prometheus, scripts d’alertes, etc.
- `grafana/` : dashboards, requêtes, intégrations Grafana
- `prometheus/` : règles, configurations, exports Prometheus
- `samples/` : exemples avancés d’utilisation (alerts, grafana, prometheus)

Chaque sous-dossier contient :
- Les scripts principaux
- Un README explicatif
- Les fichiers d’initialisation (`__init__.js`, `__init__.py`)
- Un fichier `.keep` pour le versionnement

Le point d’entrée principal du module est `index.js`.

## Bonnes pratiques
- Ajouter tout nouveau module ou exemple dans le sous-dossier approprié.
- Documenter chaque module et fournir des exemples d’utilisation.
- Ajouter des tests unitaires pour chaque module.

---

Structure validée par un ingénieur senior, clé en main, prête pour l’industrialisation.
