# migrations/versions

Documentation interne Dihya Coding.

## Objectif

Ce dossier contient les scripts de migration de base de données versionnés (ex : Alembic pour SQLAlchemy).
Il permet de suivre l’évolution du schéma, d’appliquer ou de revenir à une version précise, et d’assurer la traçabilité des changements.

## Bonnes pratiques Dihya Coding

- **Versionner chaque migration** avec un nom explicite et un timestamp.
- **Documenter chaque script** (but, impact, dépendances éventuelles).
- **Ne jamais modifier une migration déjà appliquée en production** : créer une nouvelle migration pour chaque évolution.
- **Tester chaque migration** sur une base de test avant déploiement.
- **Sécuriser les scripts** : ne jamais inclure de données sensibles ou de credentials.
- **Automatiser l’application des migrations** via CI/CD (GitHub Actions).

## Exemple de nommage

```
20250515_ajout_table_user.py
20250516_modif_colonne_email.py
```

## Exemple de commande Alembic

```bash
alembic revision --autogenerate -m "Ajout table user"
alembic upgrade head
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*