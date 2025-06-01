# 📦 Dihya – Fixtures pour le module Médias

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "medias.media", "pk": 1, "fields": {"titre": "Image Test", "type": "image", "description": "Image de test", "fichier": "medias/test.jpg", "is_public": true, "uploaded_by": 1}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/medias/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
