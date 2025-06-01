# 📦 Dihya – Fixtures pour le module Publicité

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "publicite.campagnepublicitaire", "pk": 1, "fields": {"nom": "Campagne Pub 2025", "canal": "display", "budget": "1000.00", "date_debut": "2025-06-01T00:00:00Z", "date_fin": "2025-08-31T23:59:59Z", "statut": "active", "cree_par": 1}},
  {"model": "publicite.analyticspublicite", "pk": 1, "fields": {"campagne": 1, "impressions": 1000, "clics": 100, "conversions": 10}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/publicite/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
