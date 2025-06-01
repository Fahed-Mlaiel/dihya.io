# Tests d'intégration Social

Ce dossier contient les tests d'intégration pour les routes sociales du backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints sociaux (gestion profils, posts, audit, anonymisation, export, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (API sociales, export, audit)

## Exécution

```bash
npm run test:integration -- social
```

## Structure
- `test_social.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux modules sociaux.

---

# Integration Tests Social

This folder contains integration tests for Dihya backend social routes and services.

(English, Arabic, ... translations follow in code comments)
