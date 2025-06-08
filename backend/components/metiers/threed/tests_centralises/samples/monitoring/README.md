# Monitoring — Organisation des tests centralisés

Ce dossier regroupe tous les tests d’exemples (samples) pour le monitoring, organisés par sous-dossier métier :

- `alerts/` : tests d’alertes
- `grafana/` : dashboards et intégrations Grafana
- `prometheus/` : métriques et intégrations Prometheus
- `index.js` : point d’entrée centralisé ultra avancé pour tous les tests de monitoring (import dynamique, exports clé en main, métadonnées, CI/CD ready)

Chaque sous-dossier contient les fichiers de tests correspondants, prêts à être exécutés ou intégrés dans les pipelines CI/CD.

## Logique avancée
- Tous les modules sont importés dynamiquement via `index.js`.
- Métadonnées métier, couverture, auteur, date de mise à jour incluses dans chaque module.
- Structure clé en main, extensible, conforme au cahier des charges Dihya.

---

*Ajoutez ici tout nouveau test monitoring en respectant la structure et la logique métier. Dernière mise à jour : 2025-06-08.*
