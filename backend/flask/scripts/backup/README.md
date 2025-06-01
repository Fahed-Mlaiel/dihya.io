# backup/ — Scripts de sauvegarde et restauration (Dihya Coding)

Ce dossier regroupe les scripts de sauvegarde et de restauration pour le backend Flask Dihya Coding.

## Objectif

- Automatiser la sauvegarde régulière des bases de données, fichiers critiques et configurations.
- Permettre la restauration rapide et fiable en cas d’incident ou de migration.
- Garantir la sécurité, la traçabilité et la conformité des opérations de backup.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Ne jamais inclure de secrets ou de données sensibles en clair dans les scripts ou les logs.
- Logger les opérations de sauvegarde/restauration pour audit et conformité.
- Prévoir des tests ou des dry-run pour les scripts à effet destructeur.
- Chiffrer les sauvegardes contenant des données sensibles.
- Respecter la conformité RGPD et les politiques de rétention des données.

## Exemple de structure

- `backup_db.sh` : sauvegarde de la base de données.
- `restore_db.sh` : restauration de la base de données.
- `backup_files.sh` : sauvegarde des fichiers critiques (uploads, configs, etc.).
- `verify_backup.sh` : vérification de l’intégrité des sauvegardes.

## Exemple d’utilisation

```bash
bash backup_db.sh
bash restore_db.sh --file backup_2025-05-15.sql