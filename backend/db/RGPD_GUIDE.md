# Guide RGPD – Dihya Backend DB

Ce guide détaille la conformité RGPD pour la base de données Dihya.

## Exigences
- Consentement explicite (champ `consent_rgpd`)
- Suppression logique (`deleted_at`), anonymisation
- Export et purge des données sur demande
- Journalisation des accès et modifications

## Procédures
- Toujours demander le consentement RGPD à la création d’un utilisateur
- Permettre la purge/anonymisation sur demande (voir scripts RGPD)
- Tester la conformité à chaque migration et release

## Références
- Voir `migrations/`, `database_schema.sql`, `tests/`, `scripts/rgpd/`
