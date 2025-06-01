# graphql/ — API GraphQL pour Dihya Coding

Ce dossier contient les schémas, résolveurs et scripts liés à l’API GraphQL du backend Dihya Coding.

---

## Objectif

- Offrir une alternative moderne à l’API REST pour la génération, la consultation et la gestion des projets.
- Permettre des requêtes flexibles et optimisées pour le frontend ou des intégrations tierces.
- Garantir la sécurité, la conformité RGPD, la traçabilité et la souveraineté des données.

---

## Bonnes pratiques

- Définir les schémas GraphQL dans des fichiers dédiés et documentés (`schema.py`).
- Séparer la logique métier dans les résolveurs (`resolvers.py`).
- Sécuriser chaque requête/mutation : authentification JWT/OAuth2, validation des rôles, contrôle d’accès strict.
- Valider toutes les entrées côté serveur avant toute mutation ou accès critique.
- Logger chaque requête/mutation critique pour auditabilité (sans fuite de données sensibles).
- Ne jamais exposer de données sensibles, secrets, tokens ou mots de passe via GraphQL.
- Limiter la profondeur des requêtes et la taille des réponses pour éviter les abus (DoS, scraping).
- Prévoir des tests unitaires et d’intégration pour chaque résolveur et mutation.
- Documenter chaque type, champ, requête et mutation dans ce dossier via docstrings détaillées.
- Prévoir la purge et l’export des logs GraphQL pour conformité RGPD.

---

## Structure recommandée

- `schema.py` : schéma principal GraphQL (types, queries, mutations, sécurité, documentation)
- `resolvers.py` : fonctions de résolution des queries/mutations (logique métier, validation, audit)
- `README.md` : documentation, bonnes pratiques et exemples d’utilisation

---

## Exemple d’utilisation (Flask + Graphene)

```python
from flask import Flask
from flask_graphql import GraphQLView
from app.graphql.schema import schema

app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)