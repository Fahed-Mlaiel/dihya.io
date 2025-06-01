# Automobile – API Dihya

Ce module gère les routes RESTful et GraphQL pour les projets automobiles (IA, VR, AR, etc.).

- Sécurité avancée (CORS, JWT, audit, RGPD)
- Multilingue (fr, en, ar, etc.)
- Multitenancy, rôles (admin, user, invité)
- Extensible (plugins, IA fallback)
- Documentation intégrée, tests complets

Exemple d’appel :

```bash
curl -H "Authorization: Bearer <token>" https://.../api/automobile/projects
```

Langues supportées : français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

Voir `routes.py` pour l’API complète.

## Fichiers critiques
- routes.py : Endpoints REST/GraphQL
- schemas.py : Schémas Marshmallow
- plugins.py : Plugins SEO, accessibilité, RGPD, audit
- validators.py : Validateurs métier
- audit.py : Journalisation avancée
- i18n.py : Internationalisation
- services.py : Logique métier
- tests/README.md : Documentation des tests
- tests/test_routes.py : Tests avancés (REST, GraphQL, RGPD, sécurité, accessibilité, SEO, plugins, audit, multitenancy, etc.)

## Sécurité & RGPD
- Validation stricte, audit, anonymisation, export RGPD, suppression sécurisée.

## Internationalisation
- Messages multilingues (fr, en, ar).

## Plugins
- SEO, accessibilité, RGPD, audit, extensibilité.

## Tests
- Couverture complète (unitaires, intégration, e2e, sécurité, RGPD, accessibilité, SEO, plugins, audit, multitenancy, etc.).

## CI/CD
- Compatible pipelines, production-ready.
