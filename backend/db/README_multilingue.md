# Multilingue – Dihya Backend DB

Ce fichier documente la gestion multilingue dans le module DB.

## Champs multilingues
- `lang` dans `users` : fr, en, ar, tzm
- Données de test et fixtures dans chaque langue

## Bonnes pratiques
- Toujours prévoir la compatibilité multilingue dans le schéma et les migrations
- Tester l’internationalisation dans les tests unitaires

## Exemples
- Voir `fixtures_example.json` et `tests/test_multilingue.py`

---

> Voir la documentation principale dans `README.md` et les migrations dans `migrations/`.
