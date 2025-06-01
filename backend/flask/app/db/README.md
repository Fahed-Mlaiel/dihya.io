# db/ — Gestion base de données Backend Dihya Coding

Ce dossier regroupe les modules, scripts et configurations pour la gestion de la base de données du backend Flask Dihya Coding.

## Objectif
- Centraliser la connexion, l’initialisation, la migration et la gestion des modèles de données.
- Garantir la sécurité, la traçabilité, la conformité RGPD et la performance des accès DB.
- Permettre l’extension via plugins, templates métiers, scripts d’audit et de migration.

## Bonnes pratiques
- Ne jamais stocker de credentials en dur (utiliser variables d’environnement ou vault).
- Logger les accès critiques et les erreurs pour auditabilité.
- Prévoir des scripts de migration, backup, restauration et purge RGPD.
- Documenter chaque modèle, chaque migration, chaque point d’extension.
- Ajouter des tests unitaires pour chaque module critique.

## Structure recommandée
- `models.py` : Modèles de base (User, Project, Log, etc.)
- `session.py` : Initialisation et gestion de session DB
- `migrations/` : Scripts de migration (Alembic)
- `tests/` : Tests unitaires et intégration
