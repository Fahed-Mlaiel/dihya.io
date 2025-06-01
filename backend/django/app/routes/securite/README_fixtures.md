# 📦 Dihya – Fixtures pour le module Sécurité

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "securite.incidentsecurite", "pk": 1, "fields": {"titre": "Incident Test", "description": "Desc", "niveau": "mineur", "signale_par": 1, "resolu": false}},
  {"model": "securite.alertesecurite", "pk": 1, "fields": {"titre": "Alerte Test", "message": "Alerte", "niveau": "info", "actif": true}},
  {"model": "securite.controlesecurite", "pk": 1, "fields": {"nom": "Contrôle Test", "description": "Desc", "date_controle": "2025-05-01", "conforme": true}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/securite/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
