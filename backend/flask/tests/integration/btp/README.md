# Tests d'intégration : BTP

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés au BTP dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques BTP

## Structure
- `test_btp_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Construction & Public Works

This folder contains advanced integration tests for BTP routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- BTP plugins/extensions

## Structure
- `test_btp_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```

---

## Checklist métier avancée & conformité
- [ ] Sécurité avancée (CORS, JWT, WAF, anti-DDOS, RBAC)
- [ ] Internationalisation dynamique (fr, en, ar, edge-cases)
- [ ] Multitenancy, gestion des rôles (admin, chef de chantier, ouvrier, invité)
- [ ] Conformité RGPD (anonymisation, export, consentement, effacement)
- [ ] Auditabilité complète (logs structurés, horodatage, rapport d’accès)
- [ ] Plugins/extensions BTP (audit accès chantier, anonymisation, reporting)
- [ ] Extensibilité (hooks métier, DWeb/IPFS, plugins sectoriels)
- [ ] Validation automatique de la cohérence métier après chaque test
- [ ] Documentation technique et métier exhaustive
- [ ] Tests avancés (unitaires, intégration, non-régression, performance, sécurité, souveraineté, DWeb)
- [ ] Intégration CI/CD complète (tests, lint, audit, reporting, publication doc)

## Extension DWeb/IPFS
- Export des logs critiques et rapports de tests BTP sur IPFS ou stockage décentralisé
- Documentation sur la portabilité et la souveraineté des rapports de tests

## Hooks métier BTP
- Ajoutez des hooks pour déclencher des actions métier après chaque test critique (ex : notification, audit, synchronisation DWeb)

## Intégration CI/CD
Ajoutez dans `.github/workflows/ci.yml` :
```yaml
- name: Tests intégration BTP
  run: pytest backend/flask/tests/integration/btp/ --maxfail=1 --disable-warnings --cov=.
```

## Tests avancés recommandés
- Tests de sécurité (contrôle d’accès, anonymisation, effacement, injection)
- Tests de souveraineté (stockage, portabilité, effacement souverain)
- Tests DWeb/IPFS (export, intégrité, portabilité)
- Tests d’auditabilité (logs, rapports, traçabilité)
- Tests de rollback/suppression sécurisée
