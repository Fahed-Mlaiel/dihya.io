# prometheus – Monitoring

Ce dossier regroupe les helpers et intégrations Prometheus (JS, Python).
- prometheus.js / prometheus.py : helpers Prometheus

Structure professionnelle, claire, extensible.

# prometheus/

Règles, configurations et exports Prometheus pour le monitoring de sécurité.

- `__init__.js`, `__init__.py` : points d’entrée
- `.keep` : versionnement du dossier

## Bonnes pratiques
- Centraliser toute logique Prometheus ici.
- Ajouter des exemples dans `samples/prometheus/`.
