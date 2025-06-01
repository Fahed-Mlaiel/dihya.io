# Dihya Backend Django Routes Preview

Ce module gère les routes API pour la prévisualisation, sandbox, démo, etc.

## Fonctionnalités
- Génération de previews, sandbox, démos IA
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, testeur, invité)
- Intégration IA (génération de démos, analyse)
- Plugins (connecteurs démo, reporting)

## Exemple d'utilisation
```http
POST /api/preview/generate/
GET /api/preview/list/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
