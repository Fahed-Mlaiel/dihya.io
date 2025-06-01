# Dihya VR & AR API

---

**Langues prises en charge** : Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español

## Description
API RESTful & GraphQL pour la gestion avancée de projets VR/AR (sécurité maximale, multitenancy, plugins, RGPD, audit, SEO, IA fallback, accessibilité, export, anonymisation, logs structurés, documentation intégrée, tests complets, déploiement CI/CD, extensibilité plugins, conformité RGPD, accessibilité universelle, multilingue dynamique).

- **Endpoints principaux** :
  - `GET /api/vr_ar/projects` : Liste des projets VR/AR (filtrage multitenant, rôles, plugins, fallback IA, RGPD, export, anonymisation, accessibilité, SEO)
  - `POST /api/vr_ar/projects` : Création projet VR/AR (validation, audit, plugins, RGPD, accessibilité, SEO)
  - `POST /api/vr_ar/graphql` : Endpoint GraphQL sécurisé (requêtes avancées, plugins, audit, RGPD, SEO)

- **Sécurité** : CORS dynamique, JWT, WAF, anti-DDOS, validation, audit, RBAC, logs structurés, plugins sandboxés
- **Multitenancy & rôles** : admin, user, invité (RBAC)
- **Internationalisation** : 13+ langues dynamiques
- **Plugins** : extensibles via API/CLI
- **RGPD** : export, anonymisation, auditabilité, logs, consentement
- **SEO backend** : robots.txt, sitemap.xml, logs structurés
- **Accessibilité** : API et logs accessibles, conformité WCAG
- **IA fallback** : LLaMA, Mixtral, Mistral
- **Déploiement** : Docker, K8s, GitHub Actions, fallback local
- **Tests** : unitaire, intégration, e2e, mock, fixtures
- **Documentation** : docstring, type hints, OpenAPI/GraphQL, multilingue

## Exemple d’appel
```bash
curl -H "Authorization: Bearer <token>" https://<host>/api/vr_ar/projects
```

## Contribution
- Compatible GitHub Codespaces, Linux, CI
- Voir CONTRIBUTING.md
