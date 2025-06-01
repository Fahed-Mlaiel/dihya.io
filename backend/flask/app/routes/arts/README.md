# Arts – API Dihya

Ce module gère les routes RESTful et GraphQL pour les projets artistiques (IA, VR, AR, etc.).

- Sécurité avancée (CORS, JWT, audit, RGPD)
- Multilingue (fr, en, ar, etc.)
- Multitenancy, rôles (admin, user, invité)
- Extensible (plugins, IA fallback)
- Documentation intégrée, tests complets

Exemple d’appel :

```bash
curl -H "Authorization: Bearer <token>" https://.../api/arts/projects
```

Langues supportées : français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

Voir `routes.py` pour l’API complète.
