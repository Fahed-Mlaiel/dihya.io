# Dihya Backend Django Routes Assurance

Ce module gère les routes API pour les projets d'assurance (auto, santé, habitation, IA, etc.).

## Fonctionnalités
- Gestion des contrats, sinistres, devis, IA prédictive
- Sécurité avancée (auth, audit, WAF, RGPD)
- Multilingue (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh)
- RESTful & GraphQL
- Gestion des rôles (admin, agent, assuré, invité)
- Intégration IA (scoring, détection fraude)
- Plugins (connecteurs assureurs, export)

## Exemple d'utilisation
```http
POST /api/assurance/contrats/
GET /api/assurance/sinistres/
```

## Sécurité
Toutes les routes sont protégées (auth, validation, audit, anti-DDOS).

## Documentation
Voir docstrings dans chaque fichier Python.
