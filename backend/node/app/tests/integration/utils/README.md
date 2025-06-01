# Tests d'intégration Utils

Ce dossier contient les tests d'intégration pour les utilitaires backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints utilitaires (logs, audit, anonymisation, export, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (API utilitaires, export, audit)

## Exécution

```bash
npm run test:integration -- utils
```

## Structure
- `test_utils.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux modules utilitaires.

---

# Integration Tests Utils

This folder contains integration tests for Dihya backend utils routes and services.

(English, Arabic, ... translations follow in code comments)
