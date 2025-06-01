# Sécurité – Tests d'intégration

Ce dossier contient les tests d'intégration pour toutes les routes et services liés à la sécurité de la plateforme Dihya (CORS, JWT, WAF, anti-DDOS, RBAC, audit, etc.).

## Objectifs
- Vérifier la conformité RGPD, l'auditabilité et la traçabilité.
- Tester la robustesse contre les attaques courantes (XSS, CSRF, injection, brute force, etc.).
- Valider la gestion des rôles (admin, user, invité) et le multitenancy.
- Assurer la compatibilité multi-langues (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es).
- Couvrir 100% des endpoints REST et GraphQL liés à la sécurité.

## Structure
- `test_securite_django.py` : tests automatisés (unitaires, intégration, e2e, mocks, fixtures).
- `policy.md` : politiques de sécurité, exigences RGPD, bonnes pratiques.

## Exécution
```bash
pytest --tb=short -v test_securite_django.py
```

## Documentation
Chaque test est documenté (docstring, type hints) et suit les standards Dihya (sécurité, accessibilité, audit, SEO, i18n).

---

# Security – Integration Tests (EN)

This folder contains all integration tests for Dihya's security features (CORS, JWT, WAF, anti-DDOS, RBAC, audit, etc.).

See above for details. All tests are fully documented and production-ready.

