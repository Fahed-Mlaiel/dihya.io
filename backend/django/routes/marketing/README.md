# Dihya Backend Django Routes Marketing

Ce module gère les routes API pour les projets marketing, campagnes, IA, etc.

## Fonctionnalités
- Gestion de campagnes, leads, IA scoring
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, marketeur, client, invité)
- Intégration IA (scoring, recommandation)
- Plugins (connecteurs CRM, emailing)

## Exemple d'utilisation
```http
POST /api/marketing/campagnes/
GET /api/marketing/leads/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
