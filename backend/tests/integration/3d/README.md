# 3D – Tests d'intégration avancés

## Description
Tests d'intégration pour les routes, plugins et modules 3D (IA, VR, AR, XR) du backend Dihya. Sécurité maximale (CORS, JWT, WAF, anti-DDOS), multitenancy, internationalisation dynamique (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh), conformité RGPD, auditabilité, SEO backend, plugins IA fallback (LLaMA, Mixtral, Mistral), logs structurés, accessibilité, extensibilité.

## Exemples de tests
- Authentification JWT multi-rôles (admin, user, invité)
- Validation CORS et WAF
- Génération dynamique de scènes 3D (API REST/GraphQL)
- Export anonymisé RGPD
- Fallback IA open source
- Vérification accessibilité (a11y)

## Structure type
- `test_3d_routes.py` : tests API REST/GraphQL 3D
- `test_3d_plugins.py` : tests plugins/extensibilité
- `fixtures_3d.json` : jeux de données multilingues

## Instructions CI/CD
- Exécution via GitHub Actions, Docker, K8s, fallback local
- Compatible Codespaces/Linux/CI

## Multilingue
- Toutes les assertions et logs sont localisés (fr, en, ar, etc.)

## Contribution
- Ajoutez vos tests en respectant la structure, la sécurité, la conformité RGPD et l'internationalisation.

---

# 3D – Advanced Integration Tests (EN)

## Description
Integration tests for 3D backend routes, plugins, and modules (AI, VR, AR, XR). Maximum security (CORS, JWT, WAF, anti-DDOS), multitenancy, dynamic i18n, GDPR compliance, auditability, SEO, fallback open-source AI, structured logs, accessibility, extensibility.

## Test Examples
- JWT multi-role authentication (admin, user, guest)
- CORS and WAF validation
- Dynamic 3D scene generation (REST/GraphQL)
- GDPR-compliant anonymized export
- Open-source AI fallback
- Accessibility (a11y) checks

## Structure
- `test_3d_routes.py`: REST/GraphQL API tests
- `test_3d_plugins.py`: plugin/extensibility tests
- `fixtures_3d.json`: multilingual test data

## CI/CD
- Run via GitHub Actions, Docker, K8s, local fallback
- Codespaces/Linux/CI compatible

## Multilingual
- All assertions/logs localized (fr, en, ar, etc.)

## Contribution
- Add tests respecting structure, security, GDPR, and i18n.
