# Dihya Backend Django Routes Journalisme

Ce module gère les routes API pour les projets de journalisme, médias, IA, etc.

## Fonctionnalités
- Gestion d'articles, reportages, IA rédactionnelle
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, journaliste, lecteur, invité)
- Intégration IA (génération de contenu, analyse de fake news)
- Plugins (connecteurs CMS, réseaux sociaux)

## Exemple d'utilisation
```http
POST /api/journalisme/articles/
GET /api/journalisme/reportages/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
