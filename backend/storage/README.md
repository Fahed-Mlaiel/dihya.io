# Dihya Backend – Storage

Ce dossier gère le stockage des fichiers, blobs, documents, uploads, backups, etc. pour le backend Dihya.

## Objectifs
- Stockage sécurisé, souverain, auditable
- Support multi-backend (local, S3, MinIO, cloud souverain)
- Conformité RGPD (logs, purge, anonymisation)
- Accessibilité et multilingue (fr, en, ar, tzm)

## Structure recommandée
- uploads/ : fichiers uploadés par les utilisateurs
- backups/ : sauvegardes chiffrées
- temp/ : fichiers temporaires, nettoyage automatique
- logs/ : logs d’accès et d’audit

## Bonnes pratiques
- Toujours chiffrer les données sensibles
- Limiter les accès (RBAC, logs)
- Purger régulièrement les fichiers temporaires

---

> Voir la documentation principale dans `../README.md` et les scripts dans `../scripts/`.
