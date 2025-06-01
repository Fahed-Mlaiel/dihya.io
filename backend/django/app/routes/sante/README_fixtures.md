# 📦 Dihya – Fixtures pour le module Santé

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "sante.patient", "pk": 1, "fields": {"nom": "Doe", "prenom": "Jane", "date_naissance": "1990-01-01", "email": "jane.doe@example.com", "telephone": "0102030405", "genre": "femme"}},
  {"model": "sante.rendezvous", "pk": 1, "fields": {"patient": 1, "date": "2025-06-01T10:00:00Z", "motif": "Consultation", "statut": "planifie"}},
  {"model": "sante.dossiermedical", "pk": 1, "fields": {"patient": 1, "description": "Dossier test", "date_ouverture": "2025-05-01", "actif": true}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/sante/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
