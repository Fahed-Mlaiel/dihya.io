# Dihya Backend Django Routes Ressources Humaines

Ce module gère les routes API pour les projets RH, recrutement, IA, etc.

## Fonctionnalités
- Gestion de candidatures, offres, IA matching
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, RH, candidat, invité)
- Intégration IA (matching, scoring, anonymisation)
- Plugins (connecteurs SIRH, jobboards)

## Exemple d'utilisation
```http
POST /api/ressources_humaines/candidatures/
GET /api/ressources_humaines/offres/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
