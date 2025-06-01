# Guide Sécurité – Dihya Backend Storage

Ce guide détaille les bonnes pratiques de sécurité pour le stockage des fichiers backend.

## Exigences
- Chiffrement des fichiers sensibles (AES-256, GPG)
- Accès restreint (RBAC, logs)
- Journalisation des accès et modifications
- Conformité RGPD (purge, anonymisation, logs)

## Procédures
- Toujours chiffrer les backups et uploads critiques
- Limiter les accès aux dossiers sensibles
- Purger régulièrement les fichiers temporaires et orphelins

## Références
- Voir `backups/`, `uploads/`, `logs/`, `temp/`, `../../scripts/`
