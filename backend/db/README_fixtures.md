# Fixtures – Dihya Backend DB

Ce fichier documente l’utilisation des fixtures pour les tests et la conformité RGPD.

## Objectifs
- Fournir des jeux de données anonymisés, multilingues, RGPD-ready
- Tester l’import/export, la migration, la suppression logique

## Bonnes pratiques
- Toujours anonymiser les données de test
- Couvrir tous les cas critiques (fr, en, ar, tzm)

## Exemple
Voir `fixtures_example.json` et `tests/test_fixtures.py`
