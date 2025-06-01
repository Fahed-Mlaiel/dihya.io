# Tests du module AI – Dihya Backend

Ce dossier contient l’ensemble des tests unitaires, d’intégration, e2e, sécurité, RGPD, accessibilité et plugins pour le module AI.

## Structure
- `test_routes.py` : tests avancés des routes REST/GraphQL, sécurité, RGPD, plugins, accessibilité, SEO, multitenancy.
- (Ajouter ici tout nouveau fichier de test ou fixture spécifique au module AI)

## Exécution des tests

```bash
pytest test_routes.py
```

## Bonnes pratiques
- Couvrir tous les cas métier, sécurité, RGPD, accessibilité, multilingue, plugins, audit.
- Utiliser des fixtures, mocks, et tests e2e si besoin.
- Respecter la structure et la logique métier du projet Dihya.

## Documentation
- [Guide de tests Dihya](../../../../../E2E_TESTS_GUIDE.md)
- [README global](../../../../../README.md)

# Tests avancés du module AI

Ce dossier contient des tests unitaires, d’intégration, d’accessibilité et de conformité RGPD pour le module métier AI du backend Flask Dihya.

- Sécurité, RGPD, accessibilité, plugins, audit, i18n, edge cases, CI/CD.
- Couverture exhaustive : REST, GraphQL, multitenancy, SEO, etc.
- Voir `test_routes.py` pour les cas d’usage principaux.

---
© Dihya 2025 – Tests inclusifs, sécurité, RGPD, accessibilité, production-ready.
