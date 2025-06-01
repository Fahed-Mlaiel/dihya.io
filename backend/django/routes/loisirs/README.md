# Dihya Backend Django Routes Loisirs

Ce module gère les routes API pour les projets loisirs, événements, IA, etc.

## Fonctionnalités
- Gestion d'événements, réservations, IA recommandation
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, organisateur, participant, invité)
- Intégration IA (recommandation, analyse de tendances)
- Plugins (connecteurs billetterie, réseaux sociaux)

## Exemple d'utilisation
```http
POST /api/loisirs/evenements/
GET /api/loisirs/reservations/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
