# Guide de tests pour le module VR/AR

## Objectif
Ce document décrit les stratégies de tests (unitaires, intégration, e2e) pour garantir la robustesse, la sécurité, la conformité RGPD et la performance du module vr_ar.

## Stratégies de tests
- **Unitaires** : chaque serializer, modèle, vue, permission, tâche, etc.
- **Intégration** : création de scène, gestion d’assets, audit, RGPD, accessibilité.
- **E2E** : scénarios utilisateur (création, visualisation, suppression, audit, export RGPD, etc.)

## Bonnes pratiques
- Couverture > 95% lignes/branches
- Tests multilingues (fr, en, ar, amazigh)
- Tests d'accessibilité (API, assets)
- Tests de sécurité (auth, permissions, injection, XSS, CSRF, etc.)
- Tests de performance (création, visualisation, export)

## Exemples
- test_create_scene_fr
- test_view_asset_arabic
- test_permission_denied
- test_rgpd_export

Voir le dossier tests/ pour les cas détaillés et scripts automatisés.
