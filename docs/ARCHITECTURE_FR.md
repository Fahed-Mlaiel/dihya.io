# Architecture Dihya (FR)

## Vue d’ensemble
Dihya est une plateforme souveraine, ultra-sécurisée, multi-tenant, multilingue pour la génération de projets IA, VR, AR, Voice, Web/Mobile.

### Principes clés
- API RESTful + GraphQL, système de plugins, i18n dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, audit, RGPD)
- Multi-stack : backend, frontend, mobile, VR/AR, scripts
- Extensible : plugins via API/CLI, modules métiers personnalisés
- SEO, accessibilité, auditabilité, export, anonymisation
- 100% compatible Codespaces/Linux/CI

### Composants principaux
- API Gateway (FastAPI/Flask, GraphQL, OpenAPI)
- Auth & RBAC/ABAC (JWT, multi-tenant, admin/user/invité)
- Générateur de projets (web, mobile, IA, VR/AR, Voice)
- Moteur de plugins (chargement dynamique, API/CLI)
- Audit/Logs (structurés, exportables, anonymisables)
- CI/CD (GitHub Actions, Docker, K8s, fallback local)

### Voir ARCHITECTURE_DIAGRAM.png pour le schéma complet.
