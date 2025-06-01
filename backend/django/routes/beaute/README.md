# Dihya Backend Django Routes Beauté

Ce module gère les routes API pour les projets beauté, bien-être, cosmétique, IA beauté, etc.

## Fonctionnalités
- Gestion des rendez-vous, produits, conseils IA
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, pro, client, invité)
- Intégration IA (recommandation, analyse de peau)
- Plugins (connecteurs salons, e-commerce)

## Exemple d'utilisation
```http
POST /api/beaute/rdv/
GET /api/beaute/produits/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
