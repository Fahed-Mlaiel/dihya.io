# Routes API VR/AR

## REST
- `GET /api/vr_ar/experiences` : Liste des expériences (filtres, i18n, SEO)
- `POST /api/vr_ar/experiences` : Création d’expérience (validation, audit, RBAC)
- `GET /api/vr_ar/assets` : Accès aux assets immersifs (logs, sécurité)

## GraphQL
- `POST /graphql` : Requêtes personnalisées VR/AR (sécurité, plugins, i18n)

## Sécurité
- CORS, JWT, WAF, anti-DDOS, audit logging, RBAC
- Plugins sécurité (ex : anti-plagiat, anonymisation)

## Internationalisation
- Support dynamique multilingue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Traductions IA fallback

## RGPD & Auditabilité
- Anonymisation, export, logs structurés

## SEO & Accessibilité
- Sitemap dynamique, robots.txt, logs SEO, respect WCAG

## Exemples de requêtes
```http
GET /api/vr_ar/experiences?lang=fr
POST /api/vr_ar/experiences { "name": "Visite Musée VR", "lang": "en" }
POST /graphql { "query": "{ vrArExperiences(lang: \"ar\") { id name } }" }
```

## Structure prête à l’emploi
- Code, tests, assets, configs, docs, plugins, policies, etc.
