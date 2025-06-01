# Guide de tests pour le module Voice

## Objectif
Ce document décrit les stratégies de tests (unitaires, intégration, e2e) pour garantir la robustesse, la sécurité, la conformité RGPD et la performance du module voice.

## Stratégies de tests
- **Unitaires** : chaque serializer, modèle, vue, permission, tâche, etc.
- **Intégration** : upload, transcription, audit, RGPD, accessibilité.
- **E2E** : scénarios utilisateur (upload, transcription, suppression, audit, export RGPD, etc.)

## Bonnes pratiques
- Couverture > 95% lignes/branches
- Tests multilingues (fr, en, ar, amazigh)
- Tests d'accessibilité (API, assets)
- Tests de sécurité (auth, permissions, injection, XSS, CSRF, etc.)
- Tests de performance (upload, transcription, export)

## Exemples
- test_upload_audiofile_fr
- test_transcription_arabic
- test_permission_denied
- test_rgpd_export

Voir le dossier tests/ pour les cas détaillés et scripts automatisés.
