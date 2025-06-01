# Dihya Backend Django Routes 3D

Ce module gère les routes API pour les projets 3D, VR, AR, métavers, etc.

## Fonctionnalités
- Création, gestion, visualisation de projets 3D/VR/AR
- Sécurité avancée (JWT, CORS, audit, WAF)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- Support RESTful & GraphQL
- Gestion des rôles (admin, user, invité)
- Intégration IA (génération de scènes, assets, scripts)
- Plugins extensibles (ex : import/export formats 3D, connecteurs Unity/Unreal)
- RGPD, logs structurés, anonymisation

## Exemple d'utilisation
```http
POST /api/3d/projects/ { "name": "Projet VR", "lang": "fr" }
GET /api/3d/projects/{id}/
```

## Extension
Ajoutez vos propres plugins via l'API ou le CLI (voir dossier plugins/).

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
