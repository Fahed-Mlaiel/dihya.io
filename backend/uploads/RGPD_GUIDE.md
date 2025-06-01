# Guide RGPD – Dihya Backend Uploads

Ce guide détaille la conformité RGPD pour la gestion des fichiers uploadés.

## Exigences
- Consentement explicite pour chaque upload
- Journalisation des accès, rejets, suppressions
- Purge des fichiers sur demande utilisateur
- Anonymisation des logs et métadonnées

## Procédures
- Toujours demander le consentement RGPD avant upload
- Permettre la purge/anonymisation sur demande
- Purger les logs et fichiers selon la politique de rétention

## Références
- Voir `logs/`, `rejected/`, `temp/`, `../../scripts/rgpd/`
