# Mode API & Routes

**Langues :** Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español

## Description
Gestion mode avancée pour projets IA, VR, AR, etc. Sécurité maximale, multitenant, plugins, RGPD, audit, SEO, IA fallback.

- REST & GraphQL
- Sécurité (CORS, JWT, WAF, anti-DDOS, audit)
- Multilingue dynamique
- Multitenancy & rôles (admin, user, invité)
- Plugins extensibles
- RGPD, logs, anonymisation, export
- SEO backend (robots, sitemap, logs)
- Déploiement Docker/K8s/GitHub Actions

## Endpoints principaux
- `GET /mode` : Liste mode
- `POST /mode` : Créer une entrée
- `PUT /mode/:id` : Modifier
- `DELETE /mode/:id` : Supprimer
- `POST /mode/plugin` : Plugins dynamiques

## Exemple d'appel
```bash
curl -H "Authorization: Bearer <token>" https://<host>/mode
```

## Tests
- Unitaire, intégration, e2e, mock, fixtures

## RGPD
- Export, anonymisation, auditabilité

## SEO
- Sitemap dynamique, robots.txt, logs structurés

## IA
- Fallback LLaMA, Mixtral, Mistral

## Contribution
- Compatible GitHub Codespaces, Linux, CI
- Voir CONTRIBUTING.md
