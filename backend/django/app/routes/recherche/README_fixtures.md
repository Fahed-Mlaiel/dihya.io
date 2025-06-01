# 📦 Dihya – Fixtures pour le module Recherche

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "recherche.requeterecherche", "pk": 1, "fields": {"terme": "Test", "utilisateur": 1}},
  {"model": "recherche.resultatrecherche", "pk": 1, "fields": {"requete": 1, "titre": "Résultat Test", "url": "https://example.com", "score": 0.99}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/recherche/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
