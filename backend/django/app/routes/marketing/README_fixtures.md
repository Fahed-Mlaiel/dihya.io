# 📦 Dihya – Fixtures pour le module Marketing

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "marketing.campagne", "pk": 1, "fields": {"nom": "Campagne Été 2025", "canal": "email", "audience": 1, "contenu": "Promo été", "date_debut": "2025-06-01T00:00:00Z", "date_fin": "2025-08-31T23:59:59Z", "statut": "active", "cree_par": 1}},
  {"model": "marketing.lead", "pk": 1, "fields": {"nom": "Amina", "email": "amina@example.com", "source": "landing_page", "campagne": 1}},
  {"model": "marketing.audience", "pk": 1, "fields": {"nom": "Audience Été", "description": "Cible estivale", "cree_par": 1}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/marketing/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
