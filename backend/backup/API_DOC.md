# Documentation API Backup avancé Dihya

## Endpoints REST
- `POST /backup` : Crée une sauvegarde sécurisée d’un projet.
  - Sécurité JWT, audit, multitenancy, plugins, RGPD, i18n, SEO logs.
  - Body :
    - `project_id` (str)
    - `user_id` (str)
    - `tenant_id` (str, optionnel)
    - `options` (dict, optionnel)
  - Headers :
    - `Authorization: Bearer <token>`
    - `Accept-Language: fr|en|ar|...`
  - Réponse :
    - `status` (str)
    - `message` (str, localisé)
    - `backup_id` (str)

## GraphQL (exemple)
- `mutation { createBackup(...) { status, message, backupId } }`

## Sécurité
- JWT obligatoire, CORS, WAF, anti-DDOS (à activer dans l’app principale)
- Audit structuré, logs RGPD, anonymisation

## Plugins
- Ajoutez vos plugins dans `PLUGINS` (voir `backup_service.py`)

## RGPD
- Export, anonymisation, logs, auditabilité

## SEO
- robots.txt, sitemap.xml, logs structurés

## IA fallback
- LLaMA, Mixtral, Mistral (intégration possible)

## Multitenancy
- Gestion des tenants, rôles admin/user/guest

## Tests
- Voir `tests/`, `conftest.py`, `test.py`, `test.js`

## Contact & Contribuer
- Voir CONTRIBUTING.md, CODE_OF_CONDUCT.md
