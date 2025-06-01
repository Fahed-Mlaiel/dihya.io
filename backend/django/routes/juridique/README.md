# Dihya Backend Django Routes Juridique

Ce module gère les routes API pour les projets juridiques, gestion de contrats, IA, etc.

## Fonctionnalités
- Gestion de contrats, dossiers, IA juridique
- Sécurité maximale (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, avocat, client, invité)
- Intégration IA (analyse, génération de contrats)
- Plugins (connecteurs cabinets, export)

## Exemple d'utilisation
```http
POST /api/juridique/contrats/
GET /api/juridique/dossiers/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
