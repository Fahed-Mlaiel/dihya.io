# Dihya Backend Django Routes Médias

Ce module gère les routes API pour les projets médias, diffusion, IA, etc.

## Fonctionnalités
- Gestion de contenus, diffusion, IA recommandation
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, éditeur, lecteur, invité)
- Intégration IA (recommandation, analyse de tendances)
- Plugins (connecteurs CMS, réseaux sociaux)

## Exemple d'utilisation
```http
POST /api/medias/contenus/
GET /api/medias/diffusion/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
