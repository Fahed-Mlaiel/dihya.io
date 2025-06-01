# 3D Routes – Dihya Coding

## Endpoints RESTful
- `POST /api/3d/projects` : Créer un projet 3D (sécurité, audit, RGPD, plugins, i18n)
- `GET /api/3d/projects` : Lister les projets 3D (sécurité, i18n, multitenancy)
- `PUT /api/3d/projects/:id` : Modifier un projet 3D (sécurité, audit, RGPD)
- `DELETE /api/3d/projects/:id` : Supprimer un projet 3D (sécurité, audit, anonymisation RGPD)
- `POST /api/3d/graphql` : Endpoint GraphQL 3D (sécurité, i18n, plugins)
- `GET /api/3d/seo/robots.txt` : SEO robots.txt (SEO backend)
- `GET /api/3d/rgpd/export` : Export RGPD (sécurité, audit, anonymisation)
- `GET /api/3d/audit-log` : Audit log (sécurité, auditabilité)
- `POST /api/3d/plugins/:pluginName/run` : Exécuter un plugin 3D (sécurité, plugins dynamiques, audit)

## Sécurité & RGPD
- JWT obligatoire, CORS dynamique, logs auditables, export RGPD, anonymisation, plugins sandboxés, fallback IA open source

## Multilingue
- Français, English, العربية, ⵜⴰⵎⴰⵣⵉⵖⵜ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español.

## Plugins & Extensibilité
- Ajout, exécution, audit, RGPD, extension API/CLI, fallback IA

## Tests
- Couverture unitaire, intégration, e2e, accessibilité, SEO, RGPD, plugins, fallback IA

---

Pour toute extension, voir la documentation technique, les tests et la docstring de chaque route ou plugin.
