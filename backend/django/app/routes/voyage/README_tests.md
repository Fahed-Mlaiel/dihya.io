# Guide de tests pour le module Voyage

## Objectif
Ce document décrit les stratégies de tests (unitaires, intégration, e2e) pour garantir la robustesse, la sécurité, la conformité RGPD et la performance du module voyage.

## Stratégies de tests
- **Unitaires** : chaque serializer, modèle, vue, permission, tâche, etc.
- **Intégration** : réservation, gestion, audit, RGPD, accessibilité.
- **E2E** : scénarios utilisateur (réservation, annulation, audit, export RGPD, etc.)

## Bonnes pratiques
- Couverture > 95% lignes/branches
- Tests multilingues (fr, en, ar, amazigh)
- Tests d'accessibilité (API, assets)
- Tests de sécurité (auth, permissions, injection, XSS, CSRF, etc.)
- Tests de performance (réservation, export)

## Exemples
- test_create_reservation_fr
- test_cancel_reservation_arabic
- test_permission_denied
- test_rgpd_export

Voir le dossier tests/ pour les cas détaillés et scripts automatisés.
