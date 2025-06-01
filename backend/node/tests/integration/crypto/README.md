# Tests d'intégration pour le module Crypto

## Objectif
Ce dossier contient des tests d'intégration avancés pour toutes les routes, plugins et modules liés à la gestion de projets dans le secteur crypto (blockchain, NFT, DeFi, etc.) de la plateforme Dihya.

## Exigences
- Couverture complète des API REST et GraphQL (CRUD, multitenancy, rôles, sécurité maximale, i18n, RGPD, audit, plugins, fallback IA, etc.)
- Utilisation de fixtures, mocks, et données multilingues (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Vérification de la conformité RGPD, auditabilité, anonymisation, exportabilité
- Tests d'intégration avec les services IA (LLaMA, Mixtral, Mistral)
- Tests de sécurité (CORS, JWT, WAF, anti-DDOS, validation, logs structurés)
- Exemples de requêtes et réponses pour chaque endpoint
- Prêt à l'emploi pour CI/CD, Codespaces, Docker, K8s

## Structure
- `test_crypto_api.integration.test.js` : tests API REST/GraphQL
- `fixtures/` : données de test multilingues et multi-rôles
- `mock_services/` : mocks IA, plugins, sécurité

## Exécution
```bash
npm run test:integration -- crypto
```

## Multilingue
Toutes les assertions et données couvrent les langues supportées par Dihya.

## Contact
Pour toute contribution, voir [CONTRIBUTING.md](../../../CONTRIBUTING.md)
