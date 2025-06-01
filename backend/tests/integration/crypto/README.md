# Crypto – Tests d'intégration avancés

## Description
Tests d'intégration pour les modules crypto (wallet, IA, blockchain, sécurité, audit, RGPD, multitenancy, plugins IA, logs structurés, SEO backend, internationalisation dynamique, etc.).

## Exemples de tests
- Authentification multi-rôles (admin, développeur, utilisateur)
- Export RGPD, anonymisation
- Vérification accessibilité (a11y)
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Plugins IA open source fallback

## Structure type
- `test_crypto_routes.py` : API REST/GraphQL
- `test_crypto_plugins.py` : plugins/extensibilité
- `fixtures_crypto.json` : jeux de données multilingues

## CI/CD
- GitHub Actions, Docker, K8s, fallback local
- Compatible Codespaces/Linux/CI

## Multilingue
- Logs et assertions localisées (fr, en, ar, etc.)

## Contribution
- Respectez la structure, la sécurité, la conformité RGPD et l'i18n.

---

# Crypto – Advanced Integration Tests (EN)

## Description
Integration tests for crypto modules (wallet, AI, blockchain, security, audit, GDPR, multitenancy, AI plugins, structured logs, backend SEO, dynamic i18n, etc.).

## Test Examples
- Multi-role authentication (admin, developer, user)
- GDPR export, anonymization
- Accessibility (a11y) checks
- Security (CORS, JWT, WAF, anti-DDOS)
- Open-source AI plugin fallback

## Structure
- `test_crypto_routes.py`: REST/GraphQL API
- `test_crypto_plugins.py`: plugin/extensibility
- `fixtures_crypto.json`: multilingual test data

## CI/CD
- GitHub Actions, Docker, K8s, local fallback
- Codespaces/Linux/CI compatible

## Multilingual
- All logs/assertions localized (fr, en, ar, etc.)

## Contribution
- Respect structure, security, GDPR, and i18n.
