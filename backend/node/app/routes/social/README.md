# Social API & Routes

**Langues :** Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español

## Description
Gestion social avancée pour projets IA, VR, AR, etc. Sécurité maximale, multitenant, plugins, RGPD, audit, SEO, IA fallback.

- REST & GraphQL
- Sécurité (CORS, JWT, WAF, anti-DDOS, audit)
- Multilingue dynamique
- Multitenancy & rôles (admin, user, invité)
- Plugins extensibles
- RGPD, logs, anonymisation, export
- SEO backend (robots, sitemap, logs)
- Déploiement Docker/K8s/GitHub Actions

## Endpoints principaux
- `GET /social` : Liste social
- `POST /social` : Créer une entrée
- `PUT /social/:id` : Modifier
- `DELETE /social/:id` : Supprimer
- `POST /social/plugin` : Plugins dynamiques

## Exemple d'appel
```bash
curl -H "Authorization: Bearer <token>" https://<host>/social
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
