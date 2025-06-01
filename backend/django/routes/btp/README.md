# Dihya Backend Django Routes BTP

Ce module gère les routes API pour les projets BTP, construction, chantiers, gestion de plans, etc.

## Fonctionnalités
- Gestion de chantiers, plans, ressources, IA prédictive
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, chef de chantier, ouvrier, invité)
- Intégration IA (optimisation, détection anomalies)
- Plugins (connecteurs ERP, BIM)

## Exemple d'utilisation
```http
POST /api/btp/chantiers/
GET /api/btp/plans/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
