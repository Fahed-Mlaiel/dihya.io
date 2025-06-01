# Tests d'intégration : Construction

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à la construction dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques construction

## Structure
- `test_construction_routes.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```

---

# Integration tests: Construction

This folder contains advanced integration tests for construction routes and modules in Dihya.

## Goals
- Security (CORS, JWT, WAF, anti-DDOS)
- Dynamic i18n
- Multitenancy, roles
- GDPR, auditability
- Construction plugins/extensions

## Structure
- `test_construction_routes.py`: API, security, i18n, plugins
- Fixtures, mocks, logs

## Run
```bash
pytest --tb=short --maxfail=1
```

---

## Checklist métier avancée & conformité
- [ ] Sécurité avancée (CORS, JWT, WAF, anti-DDOS, RBAC)
- [ ] Internationalisation dynamique (fr, en, ar, edge-cases)
- [ ] Multitenancy, gestion des rôles (admin, conducteur travaux, ouvrier, invité)
- [ ] Conformité RGPD (anonymisation, export, consentement, effacement)
- [ ] Auditabilité complète (logs structurés, horodatage, rapport d’accès)
- [ ] Plugins/extensions construction (audit accès chantier, anonymisation, reporting)
- [ ] Extensibilité (hooks métier, DWeb/IPFS, plugins sectoriels)
- [ ] Validation automatique de la cohérence métier après chaque test
- [ ] Documentation technique et métier exhaustive
- [ ] Tests avancés (unitaires, intégration, non-régression, performance, sécurité, souveraineté, DWeb)
- [ ] Intégration CI/CD complète (tests, lint, audit, reporting, publication doc)

## Extension DWeb/IPFS
- Export des logs critiques et rapports de tests construction sur IPFS ou stockage décentralisé
- Documentation sur la portabilité et la souveraineté des rapports de tests

## Hooks métier construction
- Ajoutez des hooks pour déclencher des actions métier après chaque test critique (ex : notification, audit, synchronisation DWeb)

## Intégration CI/CD
Ajoutez dans `.github/workflows/ci.yml` :
```yaml
- name: Tests intégration construction
  run: pytest backend/flask/tests/integration/construction/ --maxfail=1 --disable-warnings --cov=.
```

## Tests avancés recommandés
- Tests de sécurité (contrôle d’accès, anonymisation, effacement, injection)
- Tests de souveraineté (stockage, portabilité, effacement souverain)
- Tests DWeb/IPFS (export, intégrité, portabilité)
- Tests d’auditabilité (logs, rapports, traçabilité)
- Tests de rollback/suppression sécurisée
