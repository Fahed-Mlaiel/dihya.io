# Dihya Backend Assets – README global des logs

Ce dossier contient tous les exports de logs et d’audit générés côté backend (RGPD, sécurité, anonymisé, horodaté, multilingue, production-ready).

## Structure
- Un log par type (audit, accès, incident, intégrité, conformité, notification)
- Un log par langue critique (fr, en, ar, kab)
- Tous les logs sont anonymisés, hashés, versionnés, RGPD-ready
- README détaillé, exemples d’intégration, automatisation CI/CD

## Bonnes pratiques
- Aucun log ne doit contenir de données personnelles non anonymisées
- Archivez chaque log pour la traçabilité et l’auditabilité
- Intégrez l’audit automatique dans vos pipelines CI/CD
- Exportez les logs sur demande (RGPD, conformité, sécurité)

## Exemples d’intégration
- Python : voir audit_helper.py, export_logs.py
- Node.js : voir export_logs.js, plugin_loader.js

## Contact
support@dihya.ai
