# 📦 Dihya – Fixtures pour le module Restauration

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "restauration.restaurant", "pk": 1, "fields": {"nom": "Chez Dihya", "adresse": "1 rue de la Paix", "telephone": "0102030405", "proprietaire": 1}},
  {"model": "restauration.menu", "pk": 1, "fields": {"restaurant": 1, "nom": "Menu Test", "prix": "19.99", "disponible": true}},
  {"model": "restauration.reservation", "pk": 1, "fields": {"restaurant": 1, "client": 1, "date": "2025-06-01T19:00:00Z", "nombre_personnes": 2, "statut": "en_attente"}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/restauration/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
