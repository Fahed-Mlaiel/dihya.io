# Dihya Backend Django Routes Culture

Ce module gère les routes API pour les projets culturels, patrimoine, IA, etc.

## Fonctionnalités
- Gestion d'événements, patrimoine, IA culturelle
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, organisateur, visiteur, invité)
- Intégration IA (recommandation, analyse de tendances)
- Plugins (connecteurs musées, billetterie)

## Exemple d'utilisation
```http
POST /api/culture/evenements/
GET /api/culture/patrimoine/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
