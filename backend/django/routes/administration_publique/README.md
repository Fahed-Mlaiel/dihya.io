# Dihya Backend Django Routes Administration Publique

Ce module gère les routes API pour les projets d'administration publique (e-gov, smart city, open data, etc.).

## Fonctionnalités
- Gestion des démarches administratives, open data, transparence
- Sécurité maximale (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, agent, citoyen, invité)
- Intégration IA (analyse de documents, automatisation)
- Plugins (interopérabilité, connecteurs open data)

## Exemple d'utilisation
```http
GET /api/administration_publique/demarches/
POST /api/administration_publique/demande/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
