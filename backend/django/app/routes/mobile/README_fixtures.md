# 📦 Dihya – Fixtures pour le module Mobile

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "mobile.mobileapp", "pk": 1, "fields": {"nom": "App Test", "plateforme": "android", "version": "1.0", "date_publication": "2025-01-01T00:00:00Z", "cree_par": 1}},
  {"model": "mobile.device", "pk": 1, "fields": {"user": 1, "device_id": "dev123", "plateforme": "android"}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/mobile/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
