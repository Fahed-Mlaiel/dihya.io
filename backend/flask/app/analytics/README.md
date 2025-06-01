# analytics/ — Analytics Backend Dihya Coding

Ce dossier regroupe les modules et scripts d’analytics pour le backend Flask Dihya Coding.

## Objectif
- Collecter, agréger et exposer des métriques d’usage, de performance et de sécurité.
- Garantir la conformité RGPD (anonymisation, consentement, export/purge sur demande).
- Permettre l’extension via plugins (analytics métiers, custom, IA, etc.).

## Bonnes pratiques
- Ne jamais stocker de données personnelles sans consentement explicite.
- Logger les accès et actions critiques pour auditabilité.
- Prévoir des exports anonymisés et des scripts de purge.
- Documenter chaque module, chaque métrique, chaque point d’extension.
- Ajouter des tests unitaires pour chaque module critique.

## Structure recommandée
- `core.py` : Collecte et agrégation des métriques de base
- `plugins/` : Analytics métiers, extensions, IA
- `tests/` : Tests unitaires et intégration
