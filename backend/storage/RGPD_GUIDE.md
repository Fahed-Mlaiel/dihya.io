# Guide RGPD – Dihya Backend Storage

Ce guide détaille la conformité RGPD pour le stockage des fichiers backend.

## Exigences
- Consentement explicite pour chaque upload
- Journalisation des accès et suppressions
- Purge des fichiers sur demande utilisateur
- Anonymisation des logs et métadonnées

## Procédures
- Toujours demander le consentement RGPD avant upload
- Permettre la purge/anonymisation sur demande
- Purger les logs et fichiers selon la politique de rétention

## Références
- Voir `uploads/`, `logs/`, `../../scripts/rgpd/`
