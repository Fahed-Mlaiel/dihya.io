# Voyage – Dihya Integration Test Suite

---

**Langues :** Français | English | العربية | ⴰⵎⴰⵣⵉⵖ | Deutsch | 中文 | 日本語 | 한국어 | Nederlands | עברית | فارسی | हिन्दी | Español

---

## Présentation
Ce module fournit des tests d'intégration avancés pour la gestion de projets voyage, tourisme, IA, VR, AR dans Dihya. Il couvre la sécurité (CORS, JWT, WAF, anti-DDOS), l'audit, la conformité RGPD, la génération de routes REST/GraphQL, la gestion multitenant, l'intégration IA (LLaMA, Mixtral, Mistral), et la documentation multilingue.

## Fonctionnalités principales
- Génération automatique de routes RESTful & GraphQL pour voyage
- Sécurité maximale (CORS, JWT, WAF, audit, anti-DDOS)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, gestion des rôles (admin, user, invité)
- Intégration IA fallback (LLaMA, Mixtral, Mistral)
- Système de plugins extensible (API/CLI)
- Conformité RGPD, auditabilité, anonymisation, export
- Optimisation SEO backend (robots, sitemap, logs structurés)
- Déploiement GitHub Actions, Docker, K8s, fallback local
- 100% compatible Codespaces/Linux/CI

## Structure des tests
- **Unitaires** : validation des routes, sécurité, i18n, plugins
- **Intégration** : scénarios multi-utilisateurs, multitenant, audit
- **E2E** : déploiement, fallback IA, conformité RGPD
- **Fixtures/Mock** : données réalistes, anonymisées

## Exemples de routes testées
- `/api/voyage/trips` (CRUD, multilingue, RBAC, audit)
- `/api/voyage/bookings` (gestion, export, audit)
- `/api/voyage/plugins` (ajout dynamique, sécurité)
- `/graphql` (requêtes avancées, rôles, fallback IA)

## Exécution des tests
```bash
pytest --cov=voyage --maxfail=1 --disable-warnings
```

## Bonnes pratiques
- Respecter la structure REST/GraphQL
- Toujours valider les rôles et la sécurité
- Utiliser les fixtures multilingues
- Vérifier la conformité RGPD et l’auditabilité

## Ressources complémentaires
- [Guide Sécurité](../../../API_SECURITY_GUIDE.md)
- [Guide RGPD](../../../LEGAL_COMPLIANCE_GUIDE.md)
- [Guide Plugins](../../../PLUGINS_GUIDE.md)
- [Guide Déploiement](../../../RELEASE_CHECKLIST.md)

---

© 2025 Dihya Coding – Open Source, souveraineté numérique, extensible, production ready.
