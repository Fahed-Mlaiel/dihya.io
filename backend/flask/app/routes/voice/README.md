# Voice API routes

Ce module expose des routes REST et GraphQL pour la gestion de la voix (synthèse, reconnaissance, traduction, IA vocale, etc.)

- Sécurité maximale (CORS, JWT, WAF, audit, anti-DDOS)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Support plugins IA (LLaMA, Mixtral, Mistral, fallback open source)
- Multitenant, gestion des rôles (admin, user, invité)
- Documentation OpenAPI intégrée
- Exemples d'appels API et GraphQL
- Prêt pour production, CI/CD, Docker, K8s, Codespaces

## Exemples d'utilisation

### REST
POST /api/voice/synthesize

### GraphQL
POST /api/voice/graphql

## Sécurité
- JWT obligatoire
- Audit log
- WAF, anti-abus

## Extensibilité
- Ajout de plugins vocaux via API/CLI

## Tests
- Couverture unitaire, intégration, e2e

## Multilingue
- Toutes les réponses sont localisées dynamiquement

---

# Voice API routes

This module exposes REST and GraphQL routes for voice management (synthesis, recognition, translation, AI voice, etc.)

- Maximum security (CORS, JWT, WAF, audit, anti-DDOS)
- Multilingual (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- AI plugin support (LLaMA, Mixtral, Mistral, open source fallback)
- Multitenant, role management (admin, user, guest)
- Integrated OpenAPI documentation
- API and GraphQL usage examples
- Production-ready, CI/CD, Docker, K8s, Codespaces

## Usage examples

### REST
POST /api/voice/synthesize

### GraphQL
POST /api/voice/graphql

## Security
- JWT required
- Audit log
- WAF, anti-abuse

## Extensibility
- Add voice plugins via API/CLI

## Tests
- Unit, integration, e2e coverage

## Multilingual
- All responses are dynamically localized

---

# Module Voice (Flask)

Module métier ultra avancé pour la gestion des ressources vocales dans Dihya.

## Fonctionnalités
- API REST & GraphQL pour la gestion des voix (création, recherche, modification, suppression)
- Sécurité avancée, RGPD, accessibilité, SEO, multitenancy, plugins, audit, i18n
- Extensible, production-ready, CI/CD

## Fichiers critiques
- `services.py` : logique métier, sécurité, RGPD, plugins, audit
- `schemas.py` : schémas de données Marshmallow
- `validators.py` : validation avancée, RGPD, accessibilité
- `plugins.py` : système de plugins métier
- `audit.py` : audit logging, conformité RGPD
- `i18n.py` : internationalisation multilingue
- `README.md` : documentation exhaustive
- `tests/README.md` : doc tests avancés
- `tests/test_routes.py` : tests REST, sécurité, RGPD, accessibilité, plugins, edge cases
- `__init__.py` : import/export, extensibilité

## Sécurité & RGPD
- Contrôles d’accès, audit, anonymisation, consentement explicite

## Accessibilité & SEO
- API accessible, messages multilingues, bonnes pratiques SEO

## Extensibilité
- Plugins, hooks, schémas évolutifs

## Tests
- Couverture exhaustive, edge cases, REST, GraphQL, multitenancy, plugins, RGPD, accessibilité

## CI/CD
- Prêt pour intégration continue, déploiement automatisé
