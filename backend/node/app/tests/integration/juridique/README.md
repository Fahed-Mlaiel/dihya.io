# Tests d'intégration Juridique

Ce dossier contient les tests d'intégration pour les routes juridiques du backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints juridiques (RGPD, conformité, audit, anonymisation, export, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (services juridiques, export, audit)

## Exécution

```bash
npm run test:integration -- juridique
```

## Structure
- `test_juridique.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux modules juridiques.

---

# Integration Tests Legal

This folder contains integration tests for Dihya backend legal routes and services.

(English, Arabic, ... translations follow in code comments)
