# AI – Tests d'intégration (fusionné)

Ce dossier contient le contenu fusionné de l'ancien dossier `intelligence_artificielle`.
Toutes les références, tests et templates doivent désormais pointer ici.

---

# AI – Tests d'intégration

## Objectif
Ce dossier contient des tests d'intégration avancés pour toutes les routes, plugins et modules liés à la gestion de projets AI (LLM, NLP, computer vision, etc.) sur Dihya.

## Exigences
- Couverture complète des API REST/GraphQL (CRUD, multitenancy, rôles, sécurité, i18n, RGPD, audit, plugins, fallback AI, etc.)
- Fixtures, mocks, données multilingues (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Conformité RGPD, auditabilité, anonymisation, exportabilité
- Intégration avec AI (LLaMA, Mixtral, Mistral)
- Sécurité (CORS, JWT, WAF, anti-DDOS, validation, logs structurés)
- Exemples de requêtes/réponses pour chaque endpoint
- Prêt pour CI/CD, Codespaces, Docker, K8s

## Structure
- `test_ai_api.integration.test.js` : tests API REST/GraphQL
- `fixtures/` : données de test multilingues et multi-rôles
- `mock_services/` : mocks AI, plugins, sécurité

## Exécution
```bash
npm run test:integration -- ai
```

## Multilingue
Toutes les assertions et données couvrent les langues supportées.

## Contribution
Voir [CONTRIBUTING.md](../../../CONTRIBUTING.md)
