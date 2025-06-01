# Carte des routes métiers Dihya

Ce fichier documente la correspondance entre les modules métiers et leurs routes REST/GraphQL, avec sécurité, i18n, multitenancy, plugins, RGPD, audit, SEO, IA fallback.

| Métier         | Route REST                | Route GraphQL         | Sécurité | i18n | Multitenancy | Plugins | RGPD | SEO | IA Fallback |
|---------------|---------------------------|-----------------------|----------|------|--------------|---------|------|-----|------------|
| Manufacturing | /manufacturing            | /manufacturing/graphql| Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Marketing     | /marketing                | /marketing/graphql    | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Medias        | /medias                   | /medias/graphql       | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Mobile        | /mobile                   | /mobile/graphql       | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Mode          | /mode                     | /mode/graphql         | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Preview       | /preview                  | /preview/graphql      | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Publicité     | /publicite                | /publicite/graphql    | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |
| Recherche     | /recherche                | /recherche/graphql    | Oui      | Oui  | Oui          | Oui     | Oui  | Oui | Oui        |

## Légende
- Sécurité : CORS, JWT, WAF, anti-DDOS, validation, audit
- i18n : Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy : Gestion multi-tenant et rôles (admin, user, invité)
- Plugins : Système d’extension API/CLI
- RGPD : Audit, anonymisation, export
- SEO : Robots, sitemap, logs structurés
- IA Fallback : LLaMA, Mixtral, Mistral

> Ce mapping est généré automatiquement et extensible via plugins.
