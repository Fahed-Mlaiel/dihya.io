# Tests d'intégration IT DevOps

Ce dossier contient les tests d'intégration pour les routes et services DevOps du backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints DevOps (CI/CD, monitoring, audit, sécurité, plugins, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (GitHub Actions, Docker, K8s)

## Exécution

```bash
npm run test:integration -- it_devops
```

## Structure
- `test_it_devops.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux plugins ou modules DevOps.

---

# Integration Tests IT DevOps

This folder contains integration tests for Dihya backend DevOps routes and services.

(English, Arabic, ... translations follow in code comments)
