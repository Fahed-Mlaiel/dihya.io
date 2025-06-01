# Dihya Backend Django Routes E-commerce

Ce module gère les routes API pour les projets e-commerce, marketplaces, IA, etc.

## Fonctionnalités
- Gestion de catalogues, commandes, paiements, IA recommandation
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, vendeur, client, invité)
- Intégration IA (recommandation, scoring, détection fraude)
- Plugins (connecteurs ERP, paiement, logistique)

## Exemple d'utilisation
```http
POST /api/ecommerce/produits/
GET /api/ecommerce/commandes/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
