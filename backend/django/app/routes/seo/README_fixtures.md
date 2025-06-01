# 📦 Dihya – Fixtures pour le module SEO

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "seo.pageseo", "pk": 1, "fields": {"url": "https://example.com", "titre": "Accueil", "description": "Page d’accueil", "mots_cles": "test,seo", "indexable": true}},
  {"model": "seo.auditseo", "pk": 1, "fields": {"page": 1, "score": 95, "rapport": "OK"}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/seo/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
