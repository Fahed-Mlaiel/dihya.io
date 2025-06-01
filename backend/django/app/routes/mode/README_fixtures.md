# 📦 Dihya – Fixtures pour le module Mode

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "mode.collection", "pk": 1, "fields": {"nom": "Printemps 2025", "saison": "printemps", "annee": 2025, "cree_par": 1}},
  {"model": "mode.produit", "pk": 1, "fields": {"nom": "Robe Test", "collection": 1, "prix": "99.99", "taille": "M", "couleur": "Rouge", "disponible": true}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/mode/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
