# Dihya Backend Django Routes Recherche

Ce module gère les routes API pour les projets de recherche, laboratoires, IA, etc.

## Fonctionnalités
- Gestion de projets, publications, IA recherche
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, chercheur, lecteur, invité)
- Intégration IA (analyse, génération de rapports)
- Plugins (connecteurs laboratoires, bibliothèques)

## Exemple d'utilisation
```http
POST /api/recherche/projets/
GET /api/recherche/publications/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
