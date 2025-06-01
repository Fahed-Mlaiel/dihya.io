# Administration Publique – API Dihya

Ce module expose les routes RESTful et GraphQL pour la gestion avancée des projets d’administration publique (IA, VR, AR, etc.).

- Sécurité maximale (CORS, JWT, audit, WAF, RGPD)
- Multilingue (fr, en, ar, etc.)
- Multitenancy, rôles (admin, user, invité)
- Extensible (plugins, IA fallback)
- Documentation intégrée, tests complets

Exemple d’appel :

```bash
curl -H "Authorization: Bearer <token>" https://.../api/administration_publique/projects
```

Langues supportées : français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

Voir `routes.py` pour l’API complète.
