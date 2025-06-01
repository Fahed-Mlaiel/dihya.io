# Uploads – Dihya Backend

Ce dossier gère les fichiers uploadés par les utilisateurs (documents, images, etc.).

## Objectifs
- Sécurité, RGPD, accessibilité, souveraineté
- Journalisation, traitement, rejet, logs
- Multilingue (fr, en, ar, tzm)

## Structure
- logs/ : logs d’upload, audit, RGPD
- processed/ : fichiers validés et traités
- rejected/ : fichiers rejetés (virus, extension, RGPD)
- temp/ : fichiers temporaires

## Bonnes pratiques
- Scanner chaque fichier uploadé
- Limiter la taille et le type
- Journaliser chaque action
- Purger régulièrement

---

> Voir la documentation principale dans `../README.md` et les scripts dans `../../scripts/`.
