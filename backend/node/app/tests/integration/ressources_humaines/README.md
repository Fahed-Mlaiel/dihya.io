# Tests d'intégration Ressources Humaines

Ce dossier contient les tests d'intégration pour les routes RH du backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints RH (gestion RH, audit, anonymisation, export, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (API RH, export, audit)

## Exécution

```bash
npm run test:integration -- ressources_humaines
```

## Structure
- `test_ressources_humaines.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux modules RH.

---

# Integration Tests HR

This folder contains integration tests for Dihya backend HR routes and services.

(English, Arabic, ... translations follow in code comments)
