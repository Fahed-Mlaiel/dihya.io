# Dihya Backend Django Routes Restauration

Ce module gère les routes API pour les projets restauration, foodtech, IA, etc.

## Fonctionnalités
- Gestion de menus, commandes, IA recommandation
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, restaurateur, client, invité)
- Intégration IA (recommandation, scoring)
- Plugins (connecteurs POS, livraison)

## Exemple d'utilisation
```http
POST /api/restauration/menus/
GET /api/restauration/commandes/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
