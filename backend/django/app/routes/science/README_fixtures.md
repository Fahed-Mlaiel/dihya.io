# 📦 Dihya – Fixtures pour le module Science

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "science.projetscientifique", "pk": 1, "fields": {"titre": "Projet Test", "description": "Desc", "date_debut": "2025-01-01", "date_fin": "2025-12-31", "responsable": 1}},
  {"model": "science.publication", "pk": 1, "fields": {"projet": 1, "titre": "Publication Test", "date_publication": "2025-06-01"}},
  {"model": "science.chercheur", "pk": 1, "fields": {"nom": "Curie", "prenom": "Marie", "email": "marie.curie@example.com", "specialite": "Physique"}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/science/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
