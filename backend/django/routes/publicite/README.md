# Dihya Backend Django Routes Publicité

Ce module gère les routes API pour les projets publicité, campagnes, IA, etc.

## Fonctionnalités
- Gestion de campagnes, analytics, IA scoring
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, annonceur, client, invité)
- Intégration IA (scoring, recommandation)
- Plugins (connecteurs CRM, analytics)

## Exemple d'utilisation
```http
POST /api/publicite/campagnes/
GET /api/publicite/analytics/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
