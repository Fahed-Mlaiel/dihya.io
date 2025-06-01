# Journalisme – Tests d'intégration

## Objectif
Ce dossier contient des tests d'intégration avancés pour toutes les routes, plugins et modules liés à la gestion de projets journalistiques (rédaction, médias, fact-checking, etc.) sur Dihya.

## Exigences
- Couverture complète des API REST/GraphQL (CRUD, multitenancy, rôles, sécurité, i18n, RGPD, audit, plugins, fallback IA, etc.)
- Fixtures, mocks, données multilingues (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Conformité RGPD, auditabilité, anonymisation, exportabilité
- Intégration avec IA (LLaMA, Mixtral, Mistral)
- Sécurité (CORS, JWT, WAF, anti-DDOS, validation, logs structurés)
- Exemples de requêtes/réponses pour chaque endpoint
- Prêt pour CI/CD, Codespaces, Docker, K8s

## Structure
- `test_journalisme_api.integration.test.js` : tests API REST/GraphQL
- `fixtures/` : données de test multilingues et multi-rôles
- `mock_services/` : mocks IA, plugins, sécurité

## Exécution
```bash
npm run test:integration -- journalisme
```

## Multilingue
Toutes les assertions et données couvrent les langues supportées.

## Contribution
Voir [CONTRIBUTING.md](../../../CONTRIBUTING.md)
