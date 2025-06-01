# Dihya Backend Assets – README global datasets

Ce dossier contient tous les jeux de données d’exemple, anonymisés, multilingues, RGPD-ready, pour l’entraînement, le test, l’audit ou la validation des modèles backend.

## Structure
- users_sample.csv/.json/.yaml : utilisateurs fictifs, multilingues, anonymisés
- transactions_sample.csv : transactions fictives, multilingues, anonymisées
- audit_events_sample.yaml : événements d’audit, multilingues, anonymisés
- README détaillé, exemples d’intégration, automatisation CI/CD

## Bonnes pratiques
- Aucun dataset ne doit contenir de données personnelles réelles
- Archivez chaque version pour la traçabilité et l’auditabilité
- Intégrez la validation automatique dans vos pipelines CI/CD

## Exemples d’intégration
- Python : voir import_script.py, audit_helper.py
- Node.js : voir export_logs.js, plugin_loader.js

## Contact
support@dihya.ai
