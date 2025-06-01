# Guide Sécurité – Dihya Backend Uploads

Ce guide détaille les bonnes pratiques de sécurité pour la gestion des fichiers uploadés.

## Exigences
- Scanner chaque fichier uploadé (antivirus, extension)
- Limiter la taille et le type de fichiers
- Journaliser chaque upload, rejet, suppression
- Protéger l’accès aux fichiers et logs (RBAC)
- Conformité RGPD (logs, purge, anonymisation)

## Procédures
- Toujours scanner et valider chaque fichier
- Purger régulièrement les fichiers temporaires et rejetés
- Tester la conformité à chaque release

## Références
- Voir `logs/`, `processed/`, `rejected/`, `temp/`, `../../scripts/`
