# Politique de sécurité Dihya (français)

## Objectifs
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, audit, RGPD, anonymisation, export)
- Multitenancy, gestion des rôles (admin, user, invité)
- Plugins dynamiques, auditabilité, logs structurés
- Accessibilité, SEO, conformité CI/CD, production

## Principes
- Toutes les API requièrent JWT valide, CORS strict, WAF, audit log
- Limitation de débit, anti-abus, anti-bot, anti-DDOS
- RGPD : anonymisation, export, suppression, logs d'accès, consentement
- Plugins vérifiés, sandboxés, auditables
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Export et audit des accès sur demande

## Rôles
- **admin** : accès total, gestion plugins, audit, export, RGPD
- **user** : accès restreint, usage API, génération projets
- **invité** : accès lecture, pas d'actions critiques

## Déploiement
- CI/CD GitHub Actions, Docker, K8s, fallback local
- Logs structurés, alertes sécurité, monitoring

---

# Dihya Security Policy (English)

## Goals
- Maximum security (CORS, JWT, WAF, anti-DDOS, audit, GDPR, anonymization, export)
- Multitenancy, role management (admin, user, guest)
- Dynamic plugins, auditability, structured logs
- Accessibility, SEO, CI/CD, production compliance

## Principles
- All APIs require valid JWT, strict CORS, WAF, audit log
- Rate limiting, anti-abuse, anti-bot, anti-DDOS
- GDPR: anonymization, export, deletion, access logs, consent
- Plugins verified, sandboxed, auditable
- Multilingual (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Export and audit of accesses on request

## Roles
- **admin**: full access, plugin management, audit, export, GDPR
- **user**: restricted access, API usage, project generation
- **guest**: read-only, no critical actions

## Deployment
- CI/CD GitHub Actions, Docker, K8s, local fallback
- Structured logs, security alerts, monitoring
