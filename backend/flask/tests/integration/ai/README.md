# AI – Tests d'intégration (fusionné)

Ce dossier contient le contenu fusionné de l'ancien dossier `intelligence_artificielle`.
Toutes les références, tests et templates doivent désormais pointer ici.

---

# Tests d'intégration : AI

Ce dossier contient des tests d'intégration avancés pour les routes et modules liés à l'AI dans Dihya.

## Objectifs
- Sécurité (CORS, JWT, WAF, anti-DDOS)
- Internationalisation dynamique
- Multitenancy, gestion des rôles
- RGPD, auditabilité
- Plugins et extensions spécifiques AI

## Structure
- `test_ai_flask.py` : tests API REST/GraphQL, sécurité, i18n, plugins
- Fixtures, mocks, logs

## Exécution
```bash
pytest --tb=short --maxfail=1
```
