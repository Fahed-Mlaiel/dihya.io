# Politique de sécurité et conformité – Journalisme

## Accès & Rôles
- **admin** : accès total, audit, gestion des utilisateurs, export RGPD
- **user** : création/édition d’articles, accès restreint, audit
- **invité** : lecture publique, accès limité, logs anonymisés

## Sécurité
- CORS strict, JWT obligatoire, WAF, anti-DDOS, rate limiting
- Validation stricte des entrées (XSS, SQLi, CSRF, SSRF, RCE)
- Audit logging structuré, exportable, horodaté
- Anonymisation automatique des données sensibles
- Export RGPD sur demande

## Internationalisation
- Toutes les réponses API sont multilingues (Accept-Language)

## Plugins
- Ajout dynamique via API/CLI, sandboxing, audit

## Conformité RGPD
- Consentement explicite, droit à l’oubli, portabilité
- Logs d’accès, anonymisation, export CSV/JSON

---

# Security & Compliance Policy – Journalism

## Access & Roles
- **admin**: full access, audit, user management, GDPR export
- **user**: create/edit articles, restricted access, audit
- **guest**: public read, limited access, anonymized logs

## Security
- Strict CORS, mandatory JWT, WAF, anti-DDOS, rate limiting
- Strict input validation (XSS, SQLi, CSRF, SSRF, RCE)
- Structured, exportable, timestamped audit logging
- Automatic anonymization of sensitive data
- GDPR export on request

## Internationalization
- All API responses are multilingual (Accept-Language)

## Plugins
- Dynamic addition via API/CLI, sandboxing, audit

## GDPR Compliance
- Explicit consent, right to erasure, portability
- Access logs, anonymization, CSV/JSON export
