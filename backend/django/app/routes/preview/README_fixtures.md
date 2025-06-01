# 📦 Dihya – Fixtures pour le module Preview

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "preview.preview", "pk": 1, "fields": {"titre": "Aperçu Test", "contenu": "Contenu test", "type": "texte", "cree_par": 1}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/preview/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
