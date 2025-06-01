# Tests d'intégration Mobile

Ce dossier contient les tests d'intégration pour les routes mobiles du backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints mobiles (API mobile, notifications, génération de projets, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (API mobiles, push, plugins)

## Exécution

```bash
npm run test:integration -- mobile
```

## Structure
- `test_mobile.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux modules mobiles.

---

# Integration Tests Mobile

This folder contains integration tests for Dihya backend mobile routes and services.

(English, Arabic, ... translations follow in code comments)
