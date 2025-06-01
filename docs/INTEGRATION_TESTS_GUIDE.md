# Guide des Tests d’Intégration – Dihya Coding

Ce guide explique comment écrire, exécuter et automatiser les tests d’intégration pour garantir la sécurité, la conformité, la performance et l’accessibilité de la plateforme.

## Objectifs
- Vérifier l’interopérabilité des modules (API, plugins, i18n, sécurité, RGPD)
- Simuler des scénarios réels (multi-rôles, multi-tenants, multi-langues)
- Détecter les régressions, failles, problèmes d’accessibilité ou de performance

## Outils
- Backend : pytest, requests, faker, coverage
- Frontend : Cypress, Playwright, axe, Lighthouse
- Mocks/fixtures fournis pour chaque module

## Bonnes pratiques
- Couvrir tous les endpoints, rôles, langues, plugins
- Tester les cas extrêmes (fail sécurité, fail RGPD, fail accessibilité)
- Automatiser via CI/CD (GitHub Actions, Docker)
- Générer des rapports structurés (HTML, JSON, CSV)

## Exécution
```bash
make test-integration
```

## Structure des tests
- `tests/integration/` : scripts, fixtures, mocks, rapports
- `tests/e2e/` : scénarios bout-en-bout

---

Pour toute question, voir les guides de tests et contacter les mainteneurs.
