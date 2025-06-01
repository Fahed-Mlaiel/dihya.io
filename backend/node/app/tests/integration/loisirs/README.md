# Tests d'intégration Loisirs

Ce dossier contient les tests d'intégration pour les routes loisirs du backend Dihya.

## Objectifs
- Vérifier la conformité des endpoints loisirs (gestion d'activités, réservation, suggestions IA, etc.)
- Tester la sécurité (CORS, JWT, WAF, anti-DDOS)
- Couverture multilingue (fr, en, ar, ...)
- Vérification multitenancy et gestion des rôles
- Mock des intégrations externes (API loisirs, IA, plugins)

## Exécution

```bash
npm run test:integration -- loisirs
```

## Structure
- `test_loisirs.js` : tests d'intégration complets, mocks, fixtures, audit.

## Multilingue
Tous les messages d'erreur et de succès sont testés dans toutes les langues supportées.

## Sécurité
Tests anti-injection, anti-XSS, anti-CSRF, audit logs, anonymisation RGPD.

## Extensibilité
Ajoutez vos propres tests dans ce dossier pour couvrir de nouveaux modules loisirs.

---

# Integration Tests Leisure

This folder contains integration tests for Dihya backend leisure routes and services.

(English, Arabic, ... translations follow in code comments)
