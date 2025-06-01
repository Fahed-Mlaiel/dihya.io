# Guide Performance – Dihya Backend DB

Ce guide détaille les bonnes pratiques de performance pour la base de données Dihya.

## Exigences
- Indexation des colonnes critiques (email, username, user_id)
- Utilisation de vues pour l’audit et les accès fréquents
- Tests de performance automatisés (voir `tests/test_performance.py`)
- Optimisation des requêtes et des migrations

## Procédures
- Toujours ajouter un index pour chaque clé de recherche
- Utiliser EXPLAIN pour analyser les requêtes lentes
- Benchmarker les opérations critiques à chaque release

## Références
- Voir `migrations/`, `database_schema.sql`, `tests/`
